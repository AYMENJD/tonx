import asyncio
import json
import logging
import signal
import time
import typing
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from random import randint
from threading import current_thread, main_thread

import tonx

from . import types, utils
from .exceptions import TonXError
from .methods import TonlibFunctions
from .tonapi import TonApi

logger = logging.getLogger(__name__)

RETRYABLE_ERROR_KEYWORDS = [
    "LITE_SERVER_NETWORK",
    "block is not applied",
    "block is not ready",
]


class Client(TonlibFunctions):
    """Main client for TonX

    Args:
        config (``dict``):
            Tonlib configuration. You can get it from: https://docs.ton.org/develop/howto/compile#download-global-config.

        keystore (:class:`~tonx.types.KeyStoreType`):
            Key store type

        force_liteserver (``int``, *optional*):
            Index of lite server in ``config`` to force connect to. Default is ``None`` (up to tonlib to choose the lite server)

        library_path (``str``, *optional*):
            Path for tonlibjson shared library. Default is ``None`` (auto-lookup)

        verbosity_level (``int``, *optional*):
            Tonlib verbosity level. Default is ``2``

        loop (:py:class:`asyncio.AbstractEventLoop`, *optional*):
            Event loop. Default is ``None`` (auto-detect)
    """

    def __init__(
        self,
        config: dict,
        keystore: types.KeyStoreType,
        force_liteserver: int = None,
        library_path: str = None,
        verbosity_level: int = 2,
        loop: asyncio.AbstractEventLoop = None,
    ):
        self.config = config
        self.keystore = keystore
        self.force_liteserver = force_liteserver
        self.library_path = library_path
        self.verbosity_level = verbosity_level
        self.loop = (
            loop
            if isinstance(loop, asyncio.AbstractEventLoop)
            else asyncio.get_event_loop()
        )

        self.__check_init_args()

        self.__tonapi = TonApi(self.library_path, self.verbosity_level)
        self.__receiver_task = None
        self.__payments_instance = None
        self.__sync_event = asyncio.Event()
        self.__sync_lock = asyncio.Lock()
        self.__sync_time = 0
        self.__sync_count = 0

        self.__results = {}
        self._handlers = {}

        self.is_running = False
        self.sync_state: typing.Union[
            tonx.types.SyncStateInProgress, tonx.types.SyncStateDone
        ] = None
        self.__log_sync = False

        if isinstance(self.force_liteserver, int):
            self.config["liteservers"] = [
                self.config["liteservers"][self.force_liteserver],
            ]

        self.add_handler("updateSyncState", self.__handle_update_sync_state)

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            await self.close()
        except Exception:
            pass

    async def wait_synced(self):
        """Wait until sync state is Done"""

        await self.__sync_event.wait()

    def add_handler(
        self,
        update_type: str,
        func: typing.Callable[["tonx.Client", "tonx.types.TlObject"], typing.Any],
        position: int = None,
    ) -> None:
        """Add an update handler

        Args:
            update_type (``str``):
                An update type

            func (``Callable``):
                A callable function which takes :class:`tonx.Client` as first argument and any subclass of :class:`tonx.types.TlObject` as second argument

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            TypeError
        """

        if not isinstance(update_type, str):
            raise TypeError("update_type must be str")
        elif not isinstance(func, typing.Callable):
            raise TypeError("func must be callable")
        elif not asyncio.iscoroutinefunction(func):
            raise TypeError(
                "func must be async and accepts two arguments (client, update)"
            )
        else:
            if update_type not in self._handlers:
                self._handlers[update_type] = []

            if isinstance(position, int):
                self._handlers[update_type].insert(position, func)
            else:
                self._handlers[update_type].append(func)

    def remove_handler(self, func: typing.Callable) -> bool:
        """Remove an update handler

        Args:
            func (``Callable``):
                A callable function

        Raises:
            TypeError

        Returns:
            :py:class:`bool`: True if handler was removed, False otherwise
        """

        if not isinstance(func, typing.Callable):
            raise TypeError("func must be callable")

        for update_type in self._handlers:
            for handler in self._handlers[update_type]:
                if handler.func == func:
                    self._handlers[update_type].remove(handler)
                    self._handlers[update_type].sort(
                        key=lambda x: (x.position is None, x.position)
                    )
                    return True
        return False

    async def start(self, payments_instance: "tonx.payments.Payments" = None) -> bool:
        """Start and init TonX client

        Args:
            payments_instance (:class:`tonx.payments.Payments`, *optional*):
                Instance of :class:`tonx.payments.Payments` to start alongside ``TonX``

        Returns:
            :py:class:`bool`: ``True``, if TonX started and inited successfully
        """

        if not self.is_running:
            logger.info("Starting TonX client...")

            self.__receiver_task = self.loop.create_task(self.__receiver())

            while not self.is_running:
                await asyncio.sleep(0.5)

            res = await self.init_tonx()

            if isinstance(res, types.OptionsInfo):
                logger.info("TonX is successfully started and inited")
            else:
                logger.error(f"Incorrect init: {res}")
                raise TonXError(f"Incorrect init: {res}")

            await self.sync(request_timeout=None, wait_sync=True)

            if isinstance(payments_instance, tonx.payments.Payments):
                try:
                    await payments_instance.start()
                except Exception as e:
                    await self.close()
                    raise e
                else:
                    self.__payments_instance = payments_instance

            return True

    def run(self, payments_instance: "tonx.payments.Payments" = None) -> None:
        """Start ``TonX`` client and block until the client is closed

        Args:
            payments_instance (:class:`tonx.payments.Payments`, *optional*):
                Instance of :class:`tonx.payments.Payments` to run alongside ``TonX``
        """

        self.loop.run_until_complete(self.start(payments_instance))
        self.loop.run_until_complete(self.idle(register_signal_handlers=True))

    async def init_tonx(self):
        if isinstance(self.keystore, types.KeyStoreTypeDirectory):
            Path(self.keystore.directory).mkdir(parents=True, exist_ok=True)

        return await self.init(
            types.Options(
                config=types.Config(
                    config=json.dumps(self.config),
                    blockchain_name="",
                    use_callbacks_for_network=False,
                    ignore_cache=False,
                ),
                keystore_type=self.keystore,
            ),
        )

    async def getTransactions(
        self,
        account_address: types.AccountAddress,
        from_transaction_id: types.InternalTransactionId = None,
        to_transaction_id: types.InternalTransactionId = None,
        request_limit: int = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> typing.Union[types.Error, types.RawTransactions]:
        """
        Retrieves transactions for a specific account

        Args:
            account_address (:class:`~tonx.types.AccountAddress`):
                The account address for which to retrieve transactions

            from_transaction_id (:class:`~tonx.types.InternalTransactionId`, *optional*):
                The starting transaction ID to fetch transactions from. Default is ``None`` (last transaction)

            to_transaction_id (:class:`~tonx.types.InternalTransactionId`, *optional*):
                The ending transaction ID to fetch transactions up to. Default is ``None``

            request_limit (:py:class:`int` || :py:class:`None`, *optional*):
                Limits the number of requests made to the lite server during the retrieval process.
                If set to ``None``, there is no limit on the number of requests (infinite).
                Default is ``None``

        Returns:
            :class:`~tonx.types.RawTransactions`
        """

        if request_limit is not None and not isinstance(request_limit, int):
            raise ValueError("request_limit must be an integer or None")
        elif isinstance(request_limit, int) and request_limit < 1:
            raise ValueError("request_limit must be >= 1")

        if not from_transaction_id:
            while True:
                try:
                    accountState = await self.rawGetAccountState(
                        account_address,
                        request_timeout=request_timeout,
                        wait_sync=wait_sync,
                    )
                except asyncio.TimeoutError:
                    continue
                else:
                    if accountState.getType() == "raw.fullAccountState":
                        from_transaction_id = accountState.last_transaction_id
                        break
                    else:
                        return accountState

        if not to_transaction_id:
            to_transaction_id = types.InternalTransactionId()

        current_from_transaction_id = from_transaction_id
        transactions_list = types.RawTransactions()
        transactions_count = 0
        request_count = 0
        to_transaction_reached = False

        if from_transaction_id.lt == to_transaction_id.lt:
            return transactions_list

        while (
            request_limit is None or request_count < request_limit
        ) and not to_transaction_reached:
            try:
                raw_transactions = await self.rawGetTransactions(
                    None,
                    account_address=account_address,
                    from_transaction_id=current_from_transaction_id,
                    request_timeout=request_timeout,
                    wait_sync=wait_sync,
                )
            except asyncio.TimeoutError:
                logger.error("Timeout on rawGetTransactions request")
                await asyncio.sleep(1)
            else:
                if raw_transactions.getType() == "error":
                    if transactions_list.transactions:
                        logger.error(
                            f"raw.getTransactions returned an error after processing {transactions_count} transactions. Returning {transactions_count} transaction"
                        )
                        return transactions_list
                    else:
                        return raw_transactions
                else:
                    request_count += 1

                    if to_transaction_id.lt == 0:
                        return raw_transactions

                    for transaction in raw_transactions.transactions:
                        if transaction.transaction_id.lt <= to_transaction_id.lt:
                            to_transaction_reached = True
                            break
                        else:
                            transactions_list.transactions.append(transaction)
                            transactions_count += 1

                    if raw_transactions.previous_transaction_id:
                        if raw_transactions.previous_transaction_id.lt == 0:
                            break
                        else:
                            current_from_transaction_id = (
                                raw_transactions.previous_transaction_id
                            )
                    else:
                        break  # Just in case

        return transactions_list

    async def isArchiveNode(self, genesis_block: bool = False) -> bool:
        """
        Checks if the node is an archive node by performing a block lookup

        Args:
            genesis_block (``bool``, *optional*):
                Specifies whether to check the genesis block. Default is ``False``

        Returns:
            :py:class:`bool`: ``True`` if the node is an archive node, ``False`` otherwise
        """

        if genesis_block:
            seqno = 1
        else:
            seqno = randint(3, 4096)

        lookup = await self.blocksLookupBlock(
            mode=1,
            id=types.TonBlockId(workchain=-1, shard=-9223372036854775808, seqno=seqno),
        )

        if lookup.getType() == "ton.blockIdExt":
            return True
        else:
            return False

    async def invoke(
        self,
        request: dict,
        retries: int = 5,
        timeout: float = None,
        wait_sync: bool = False,
    ) -> typing.Union[types.Error, typing.Any]:
        """Invoke a request and return the response

        Args:
            request (``dict``):
                The request to be sent
        """

        assert self.is_running, "TonX is not running"
        assert retries > 0

        extra_id = utils.create_extra_id()
        request["@extra"] = extra_id

        if (
            logger.root.level >= logging.DEBUG
        ):  # dumping all requests may create performance issues
            logger.debug(f"Sending: {tonx.utils.obj_to_json(request, indent=4)}")

        request = tonx.utils.obj_to_json(request)

        for tries in range(retries):
            future = self.loop.create_future()
            self.__results[extra_id] = future
            self.__tonapi.send(request)

            if wait_sync:
                await self.wait_synced()

            result = await asyncio.wait_for(future, timeout=timeout)

            if result.getType() == "error" and any(
                keyword in result.message for keyword in RETRYABLE_ERROR_KEYWORDS
            ):
                logger.debug(
                    f"Retry {tries + 1}/{retries}: Got - {result.code}, {result.message}"
                )
                await asyncio.sleep(1)
            else:
                break

        return result

    async def close(self, cancel_pending_futures: bool = True):
        """Stop and close TonX

        Args:
            cancel_pending_futures (``bool``, *optional*):
                Wether to cancel all pending ``futures`` or not. Default is ``True``
        """

        if self.is_running:
            logger.info("Waiting TonX to close ...")

            if self.__payments_instance:
                await self.__payments_instance.close()

            res = await super().close()

            if res.getType() == "ok":
                logger.info("TonX closed")

                self.is_running = False
                self.__receiver_task.cancel()

                if cancel_pending_futures:
                    for _, future in self.__results.items():
                        future.cancel()
                return True
            else:
                logger.error(f"Error closing TonX: {utils.obj_to_json(res, indent=4)}")

        return False

    async def idle(self, register_signal_handlers: bool = False):
        """Idle until client is closed

        Args:
            register_signal_handlers (:py:class:`bool`, *optional*):
                Wether to register signal handlers or not. Defualt is ``False``
        """

        if register_signal_handlers:
            self._register_signal_handlers()

        while self.is_running:
            await asyncio.sleep(0.5)

    async def __handle_update_sync_state(
        self, _, new_sync_state: "tonx.types.UpdateSyncState"
    ):
        async with self.__sync_lock:
            sync_state_type = new_sync_state.sync_state.getType()

            if sync_state_type == "syncStateInProgress" and (
                not self.sync_state
                or self.sync_state.getType() != "syncStateInProgress"
            ):
                if not new_sync_state.sync_state.to_seqno:
                    return

                self.sync_state = new_sync_state.sync_state
                self.__sync_event.clear()

                seqno_count = (
                    new_sync_state.sync_state.to_seqno
                    - new_sync_state.sync_state.current_seqno
                )

                if seqno_count > 300:
                    self.__sync_time = time.time()
                    self.__sync_count = seqno_count
                    self.__log_sync = True

                    logger.info(f"Syncing {seqno_count:,} blocks...")
            elif sync_state_type == "syncStateDone":
                self.sync_state = new_sync_state.sync_state
                self.__sync_event.set()

                if self.__log_sync:
                    synced_time = time.time() - self.__sync_time

                    logger.info(
                        f"{self.__sync_count:,} block was synced in {synced_time:.2f}s"
                    )

                    self.__log_sync = False
                    self.__sync_count = 0
                    self.__sync_time = 0

    async def __process_data(self, data):
        if (
            logger.root.level >= logging.DEBUG
        ):  # dumping all results may create performance issues
            logger.debug(f"Received: {json.dumps(json.loads(data), indent=4)}")

        data = tonx.utils.json_to_obj(data)

        if data.extra_id and data.extra_id in self.__results:
            result = self.__results.pop(data.extra_id)

            if not result.done():  # To avoid ``asyncio.InvalidStateError``
                result.set_result(data)

        else:
            self.loop.create_task(self.run_handlers(data))

    async def run_handlers(self, data):
        if data.getType() in self._handlers:
            for handler in self._handlers[data.getType()]:
                try:
                    await handler(self, data)
                except Exception:
                    logger.exception(f"Calling {handler} failed")

    async def __receiver(self):
        thread = ThreadPoolExecutor(1, "TonX_receiver")
        try:
            self.is_running = True

            while self.is_running:
                data = await self.loop.run_in_executor(
                    thread, self.__tonapi.receive, 2.0  # Seconds
                )

                if not data:
                    continue

                await self.__process_data(data)
        except Exception:
            logger.exception("Exception in TonX receiver")
        finally:
            thread.shutdown(False)
            self.is_running = False

    def __check_init_args(self):
        if not isinstance(self.config, dict):
            raise TypeError("config must be dict")
        elif not issubclass(self.keystore.__class__, types.KeyStoreType):
            raise TypeError(
                "keystore must be KeyStoreTypeDirectory or KeyStoreTypeInMemory"
            )
        elif self.force_liteserver != None and not isinstance(
            self.force_liteserver, int
        ):
            raise TypeError("force_liteserver must be int or None")
        elif not isinstance(self.verbosity_level, int):
            raise TypeError("verbosity_level must be int")

    def _register_signal_handlers(self):
        def _handle_signal():
            self.loop.create_task(self.close())
            for sig in {
                signal.SIGINT,
                signal.SIGTERM,
                signal.SIGABRT,
                signal.SIGSEGV,
            }:
                self.loop.remove_signal_handler(sig)

        if current_thread() is main_thread():
            try:
                for sig in {
                    signal.SIGINT,
                    signal.SIGTERM,
                    signal.SIGABRT,
                    signal.SIGSEGV,
                }:
                    self.loop.add_signal_handler(sig, _handle_signal)
            except NotImplementedError:  # Windows dosen't support add_signal_handler
                pass
