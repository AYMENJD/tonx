import asyncio
import copy
import logging
import re
import secrets
import time
from pathlib import Path
from typing import Any, Callable, Literal, Optional, Union
from urllib.parse import quote_plus, urlparse

import tonx

try:
    import kvsqlite
except ImportError:
    kvsqlite = None

logger = logging.getLogger(__name__)

REF_TAG = "RefX#"
REF_REGEX = re.compile(REF_TAG + r"([a-zA-Z0-9_-]{11})")


def is_valid_link(link: str):
    """Checks if the input is a valid link"""

    try:
        result = urlparse(link)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


class Invoice:
    def __init__(
        self,
        invoice_address: str,
        invoice_id: str,
        amount: Union[int, float],
        payment_link: str,
        comment: str,
        created_at: int,
        ttl: Union[int, None] = None,
        extra=None,
    ):
        self.invoice_address: str = invoice_address
        """Invoice address where to send TON"""

        self.id: str = invoice_id
        """Invoice ID"""

        self.amount: Union[int, float] = amount
        """Invoice amount of TON in toncoin format"""

        self.amount_in_nanograms: int = tonx.utils.to_nanograms(amount)
        """Invoice amount of TON in nanograms"""

        self.comment: str = comment
        """Invoice comment"""

        self.ttl: Union[int, None] = ttl
        """Invoice lifetime in seconds"""

        self.created_at: int = created_at
        """Time where the invoice is created"""

        self.expire_at: int = 0 if not ttl else created_at + ttl
        """Time where the invoice will expire at"""

        self.extra = extra
        """Extra data"""

        self.is_completed: bool = False
        """``True``, if the invoice is paid and completed"""

        self.is_over_paid: bool = False
        """``True``, if the invoice is over paid (a.k.a the user paid more than the specified amount)"""

        self.paid_amount: float = 0.0
        """Paid amount for this invoice in toncoin format"""

        self.paid_in_nanograms: int = 0
        """Paid amount for this invoice in nanograms format"""

        self.paid_date: int = 0
        """Unix time paid date"""

        self.over_paid_by: float = 0.0
        """Over paid amount in toncoin format"""

        self.over_paid_by_in_nanograms: int = 0
        """Over paid amount in nanograms format"""

        self.transaction: "tonx.types.RawTransaction" = None
        """Transaction which paid this invoice. ``None`` or :class:`~tonx.types.RawTransaction`"""

        self.paid_by_address: "tonx.types.AccountAddress" = None
        """Address which paid this invoice. ``None`` or :class:`~tonx.types.AccountAddress`"""

        payment_link = payment_link.format(
            address=self.invoice_address,
            amount_in_nanograms=self.amount_in_nanograms,
            amount=amount,
            comment=quote_plus(comment),
            invoice_id=invoice_id,
        )

        if is_valid_link(payment_link):
            self.payment_link: str = payment_link
            """A link to pay this invoice"""

        else:
            raise ValueError(f"Invalid payment_link: {payment_link}")

    @property
    def is_expired(self) -> bool:
        """True, if the invoice is expired and not completed"""

        if not self.is_completed and self.expire_at:
            return time.time() > self.expire_at
        return False

    def copy(self):
        return copy.deepcopy(self)

    def to_dict(self):
        return {
            "invoice_id": self.id,
            "invoice_address": self.invoice_address,
            "amount": self.amount,
            "amount_in_nanograms": self.amount_in_nanograms,
            "comment": self.comment,
            "payment_link": self.payment_link,
            "ttl": self.ttl,
            "created_at": self.created_at,
            "expire_at": self.expire_at,
            "is_completed": self.is_completed,
            "is_expired": self.is_expired,
            "is_over_paid": self.is_over_paid,
            "paid_amount": self.paid_amount,
            "paid_in_nanograms": self.paid_in_nanograms,
            "paid_date": self.paid_date,
            "over_paid_by": self.over_paid_by,
            "over_paid_by_in_nanograms": self.over_paid_by_in_nanograms,
            "transaction": self.transaction,
            "paid_by_address": self.paid_by_address,
            "extra": self.extra,
        }


class Payments:
    """TonX payments class"""

    def __init__(
        self,
        client: "tonx.Client",
        account_address: "tonx.types.AccountAddress",
        db_path: str = "./tonx-payments/db.sqlite",
    ):
        """Init Payments class

        Args:
            client (:class:`~tonx.Client`):
                A running ``TonX`` client instance

            account_address (:class:`~tonx.types.AccountAddress`):
                An account address where payments are sent to

            db_path (``str``, *optional*):
                ``Kvsqlite`` database path. Default is ``./tonx-payments/db.sqlite``.
        """

        assert kvsqlite, "Kvsqlite not found, use `pip install kvsqlite`"
        assert isinstance(
            account_address, tonx.types.AccountAddress
        ), 'account_address must be of type "types.AccountAddress"'

        self.__raw_address = tonx.utils.Address.parse(
            account_address.account_address
        ).to_raw_string()

        self.client = client
        self.db_path = db_path
        self.__lock = asyncio.Lock()
        self.idle_sleep_interval = 5
        self.is_running = False

        self.__account_address = account_address
        self.__last_transaction = None

        self.__incoming_handlers = []
        self.__outgoing_handlers = []

        self.__payment_handlers = []

        self.__initializers = []
        self.__finalizers = []

        Path(self.db_path).resolve().parent.mkdir(parents=True, exist_ok=True)

    @property
    def account_address(self):
        """Current payments account address"""

        return self.__account_address

    @property
    def last_transaction(self):
        """Last processed transaction"""

        return self.__last_transaction

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            await self.close()
        except Exception:
            pass

    def on_incomingTransaction(
        self,
        filter_fn: Optional[
            Callable[["tonx.Client", "tonx.types.RawTransaction"], bool]
        ] = None,
    ):
        """Decorator to register an incoming transactions handler"""

        def decorator(handler):
            self.add_handler(handler, "incomingTransaction", filter_fn)
            return handler

        return decorator

    def on_outgoingTransaction(
        self,
        filter_fn: Optional[
            Callable[["tonx.Client", "tonx.types.RawTransaction"], bool]
        ] = None,
    ):
        """Decorator to register an outgoing transactions handler"""

        def decorator(handler):
            self.add_handler(handler, "outgoingTransaction", filter_fn)
            return handler

        return decorator

    def on_invoicePayment(
        self,
        filter_fn: Optional[Callable[["tonx.Client", Invoice], bool]] = None,
    ):
        """Decorator to register a payment handler"""

        def decorator(handler):
            self.add_handler(handler, "invoicePayment", filter_fn)
            return handler

        return decorator

    def initialize(
        self,
        filter_fn: Optional[
            Callable[["tonx.Client", "tonx.types.RawTransaction"], bool]
        ] = None,
    ):
        """Decorator to register an initialize handler which will be called before transaction handlers are called"""

        def decorator(initializer):
            self.add_handler(initializer, "initialize", filter_fn)
            return initializer

        return decorator

    def finalize(
        self,
        filter_fn: Optional[
            Callable[["tonx.Client", "tonx.types.RawTransaction"], bool]
        ] = None,
    ):
        """Decorator to register an finalize handler which will be called after transaction handlers are called"""

        def decorator(finalizer):
            self.add_handler(finalizer, "finalize", filter_fn)
            return finalizer

        return decorator

    def add_handler(
        self,
        handler: Union[
            Callable[["tonx.Client", "tonx.types.RawTransaction"], Any],
            Callable[["tonx.Client", Invoice], Any],
        ],
        handler_type: Literal[
            "initialize",
            "incomingTransaction",
            "outgoingTransaction",
            "invoicePayment",
            "finalize",
        ],
        filter_fn: Optional[
            Union[
                Callable[["tonx.Client", "tonx.types.RawTransaction"], bool],
                Callable[["tonx.Client", Invoice], bool],
            ]
        ] = None,
    ):
        if handler_type == "initialize":
            self.__initializers.append((handler, filter_fn))
        elif handler_type == "incomingTransaction":
            self.__incoming_handlers.append((handler, filter_fn))
        elif handler_type == "outgoingTransaction":
            self.__outgoing_handlers.append((handler, filter_fn))
        elif handler_type == "invoicePayment":
            self.__payment_handlers.append((handler, filter_fn))
        elif handler_type == "finalize":
            self.__finalizers.append((handler, filter_fn))
        else:
            raise ValueError(f"Unknown handler type: {handler_type}")

    async def start(self, reset: bool = False):
        """Start processing payments

        Args:
            reset (:py:class:`bool`, *optional*):
                If ``True``, flush the payments database and delete all invoices. Default is ``False``
        """

        assert self.client.is_running, "TonX client is not running"

        if self.is_running:
            return

        accountState = await self.client.getAccountState(
            self.__account_address, wait_sync=False
        )

        if accountState.getType() == "error":
            raise tonx.TonXError(
                f"Invalid account address {self.__account_address.account_address}: {accountState.code} - {accountState.message}"
            )

        self.__account_address = accountState.address

        self.__kv = kvsqlite.Client(self.db_path)
        if reset:
            logger.info(f"Flushing {self.db_path} database")
            await self.__kv.flush()

        self.client.loop.create_task(self.__listener())

    async def getInvoice(self, invoice_id: str) -> Union[Invoice, None]:
        """Get an Invoice by ID

        Args:
            invoice_id (:py:class:`str`):
                invoice ID

        Returns:
            :class`tonx.payments.Invoice`
            ``None``
        """

        return await self.__kv.get(f"{self.__raw_address}:invoice:{invoice_id}")

    async def createInvoice(
        self,
        amount: Union[int, float],
        comment: str = "",
        payment_link: str = "https://app.tonkeeper.com/transfer/{address}?text={comment}&amount={amount_in_nanograms}&open=1",
        ttl: Union[int, None] = 3600,
        extra=None,
    ) -> Invoice:
        """Create payment invoice

        Args:
            amount (``int`` || ``float``):
                Amount of TON in toncoin format

            comment (:class:`str`, *optional*):
                Comment that will be visible on the payment transaction. Default is empty string

            payment_link (:py:class:`str`, *optional*):
                Payment link that allow the user to pay the invoice. Default is "https://app.tonkeeper.com/transfer/{address}?text={comment}&amount={amount_in_nanograms}&open=1"

                Supported placeholders:

                            - ``{address}``: Represent the destination address

                            - ``{comment}``: Represent the comment that will be visible on the payment transaction (this comment should be included on the transaction, otherwise we cannot identify the transaction payment which will be ignored)

                            - ``{amount_in_nanograms}``: Represent the amount of TON in nanograms format

                            - ``{amount}``: Represent the amount of TON in toncoin format

                            - ``{invoice_id}``: Represent the invoice ID


            ttl (:py:class:`int`, *optional*):
                TTL of the invoice, before it gets expired. Default is ``3600`` (1 hour)

            extra (``Any``, *optional*):
                Extra data to be added to the invoice that can be accessed later with `Invoice.extra`. Useful for storing some data that can be used later (e.g User ID). Default is ``None``

        Returns:
            :class:`~tonx.payments.Invoice`
        """

        assert amount > 0.000000001, "amount must be greater than 0.000000001"
        assert isinstance(payment_link, str), "payment_link must be a string"
        assert isinstance(comment, str), "comment must be a string"

        if ttl is not None and ttl < 300:
            raise ValueError(f"ttl must be greater than 300 seconds (5 minutes)")
        elif len(comment) > 300:
            raise ValueError(f"comment must be less than 300 in length")

        async with self.__lock:
            invoice_id = await self.__create_invoice_id()
            invoice = Invoice(
                invoice_address=self.__account_address.account_address,
                invoice_id=invoice_id,
                amount=amount,
                payment_link=payment_link,
                comment=comment + f"{REF_TAG}{invoice_id}",
                ttl=ttl,
                created_at=int(time.time()),
                extra=extra,
            )

            if ttl:
                res = await self.__set_invoice(
                    invoice,
                    ttl
                    + 21600,  # 21600: keep the invoice for 6 hours after expiration.
                )  # You can handle expired invoices with ``invoice.is_expired``
            else:
                res = await self.__set_invoice(invoice)

            if res:
                return invoice
            else:
                raise RuntimeError("Could not insert invoice to database")

    async def deleteInvoice(self, invoice_id: str) -> bool:
        return await self.__kv.delete(f"{self.__raw_address}:invoice:{invoice_id}")

    async def call_handlers(
        self, handlers, data: Union["tonx.types.RawTransaction", Invoice]
    ):
        for handler, filter_fn in handlers:
            try:
                if filter_fn is None or filter_fn(self.client, data):
                    await handler(self.client, data)
            except Exception:
                logger.exception(f"Exception in {handler}:")

    async def __set_invoice(self, invoice: Invoice, ttl: int = None):
        if ttl:
            return await self.__kv.setex(
                f"{self.__raw_address}:invoice:{invoice.id}", ttl, invoice.copy()
            )
        else:
            return await self.__kv.set(
                f"{self.__raw_address}:invoice:{invoice.id}", invoice.copy()
            )

    async def __handle_payment(self, transaction: "tonx.types.RawTransaction"):
        in_msg = transaction.in_msg
        if (
            in_msg
            and in_msg.created_lt
            and in_msg.msg_data
            and in_msg.msg_data.getType() == "msg.dataText"
        ):
            invoice_id = REF_REGEX.findall(in_msg.msg_data.text.decode("utf-8"))

            if invoice_id:
                invoice_id = invoice_id[0]

                if invoice := await self.getInvoice(invoice_id):
                    if invoice.is_completed:
                        logger.warning(
                            f"Duplicated payment with invoice ID: {invoice.id} (lt: {transaction.transaction_id.lt}). Ignoring..."
                        )
                        return

                    invoice.paid_date = transaction.utime
                    invoice.paid_amount = tonx.utils.from_nanograms(in_msg.value)
                    invoice.paid_in_nanograms = in_msg.value
                    invoice.transaction = transaction
                    invoice.paid_by_address = in_msg.source

                    if in_msg.value >= invoice.amount_in_nanograms:
                        if in_msg.value > invoice.amount_in_nanograms:
                            invoice.is_over_paid = True
                            invoice.over_paid_by_in_nanograms = (
                                in_msg.value - invoice.amount_in_nanograms
                            )
                            invoice.over_paid_by = tonx.utils.from_nanograms(
                                invoice.over_paid_by_in_nanograms
                            )

                        if not invoice.is_expired:
                            invoice.is_completed = True

                    await self.__set_invoice(invoice)

                    if invoice.is_completed:
                        logger.info(
                            f"Received a complete `{tonx.utils.truncate_zeros(invoice.paid_amount)} TON` for invoice `{invoice.id}` from `{in_msg.source.account_address}`"
                        )
                    elif invoice.is_expired:
                        logger.warning(
                            f"Received payment for an expired invoice ID: {invoice.id} (lt: {transaction.transaction_id.lt})"
                        )
                    else:
                        logger.warning(
                            f"Received an incomplete amount of `{tonx.utils.truncate_zeros(invoice.paid_amount)} TON` for invoice `{invoice.id}` from `{in_msg.source.account_address}`"
                        )

                    await self.call_handlers(self.__payment_handlers, invoice)
                else:
                    logger.warning(
                        f"Ignoring payment for invoice ID {invoice_id} because its not in database"
                    )

    async def __handle_transaction(self, transaction: "tonx.types.RawTransaction"):
        for initializer, filter_fn in self.__initializers:
            try:
                if filter_fn is None or filter_fn(self.client, transaction):
                    await initializer(self.client, transaction)
            except Exception:
                logger.exception(f"Initializer {initializer} exception:")

        if (
            not transaction.out_msgs
            and transaction.in_msg
            and transaction.in_msg.created_lt
        ):
            await self.call_handlers(self.__incoming_handlers, transaction)
            try:
                await self.__handle_payment(transaction)
            except Exception:
                logger.exception("Exception while handling a payment")

        elif transaction.out_msgs:
            await self.call_handlers(self.__outgoing_handlers, transaction)
        else:
            logger.warning(f"Unrecognized transaction: {transaction}")

        for finalizer, filter_fn in self.__finalizers:
            try:
                if filter_fn is None or filter_fn(self.client, transaction):
                    await finalizer(self.client, transaction)
            except Exception:
                logger.exception(f"Finalizer {finalizer} exception:")

    async def process_transactions(self, transactions: list):
        for transaction in reversed(transactions):
            await self.__handle_transaction(transaction)

    async def __set_last_transaction(
        self, transaction: "tonx.types.InternalTransactionId"
    ):
        assert (
            isinstance(transaction, tonx.types.InternalTransactionId)
            and transaction.lt != 0
        )
        await self.__kv.set(f"{self.__raw_address}:__last_transaction", transaction)
        self.__last_transaction = transaction

    async def __get_last_transaction(self):
        return await self.__kv.get(f"{self.__raw_address}:__last_transaction")

    async def __listener(self):
        self.is_running = True

        self.__last_transaction = (
            await self.__get_last_transaction() or tonx.types.InternalTransactionId()
        )

        logger.info(
            f"Processing transactions from transaction ID: {self.last_transaction.lt}"
        )

        while self.client.is_running and self.is_running:
            try:
                rawTransactions = await self.client.getTransactions(
                    account_address=self.__account_address,
                    from_transaction_id=None,
                    to_transaction_id=self.__last_transaction,
                    request_limit=5,
                    wait_sync=False,
                )

                if rawTransactions.getType() == "error":
                    logger.error(
                        f"Error processing transactions with transaction ID {self.__last_transaction.lt}: {rawTransactions.code} - {rawTransactions.message}"
                    )
                    await asyncio.sleep(2)
                else:
                    if rawTransactions.transactions:
                        if self.__last_transaction.lt == 0:
                            await self.__set_last_transaction(
                                rawTransactions.transactions[0].transaction_id
                            )  # last transaction ID
                            continue

                        await self.__set_last_transaction(
                            rawTransactions.transactions[0].transaction_id
                        )
                        self.client.loop.create_task(
                            self.process_transactions(rawTransactions.transactions)
                        )
                    else:
                        await asyncio.sleep(self.idle_sleep_interval)

            except Exception:
                logger.exception(
                    f"Error processing transactions with transaction ID {self.__last_transaction.lt}:"
                )
                await asyncio.sleep(2)

        await self.close()

    async def __create_invoice_id(self):
        invoice_id = None

        for _ in range(20):
            secret_token = secrets.token_urlsafe(8)
            if not await self.__kv.exists(
                f"{self.__raw_address}:invoice:{secret_token}"
            ):
                invoice_id = secret_token
                break

        if not invoice_id:
            raise ValueError("No available unique ID")

        return invoice_id

    async def close(self) -> bool:
        if self.is_running:
            logger.info("Closing TonX payments")
            await self.__kv.cleanex()
            await self.__kv.close()
            logger.info("TonX payments closed")
            return True
        else:
            return False
