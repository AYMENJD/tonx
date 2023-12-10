from typing import Union, List
from .. import types


class TonlibFunctions:
    """A class that include all tonlib functions"""

    async def init(
        self,
        options: types.Options = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.OptionsInfo]:
        """Method for ``init``"""

        return await self.invoke(
            {"@type": "init", "options": options},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def close(
        self, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.Ok]:
        """Method for ``close``"""

        return await self.invoke(
            {
                "@type": "close",
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def optionsSetConfig(
        self,
        config: types.Config = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.OptionsConfigInfo]:
        """Method for ``options.setConfig``"""

        return await self.invoke(
            {"@type": "options.setConfig", "config": config},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def optionsValidateConfig(
        self,
        config: types.Config = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.OptionsConfigInfo]:
        """Method for ``options.validateConfig``"""

        return await self.invoke(
            {"@type": "options.validateConfig", "config": config},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def createNewKey(
        self,
        local_password: bytes = b"",
        mnemonic_password: bytes = b"",
        random_extra_seed: bytes = b"",
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Key]:
        """Method for ``createNewKey``"""

        return await self.invoke(
            {
                "@type": "createNewKey",
                "local_password": local_password,
                "mnemonic_password": mnemonic_password,
                "random_extra_seed": random_extra_seed,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def deleteKey(
        self,
        key: types.Key = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Ok]:
        """Method for ``deleteKey``"""

        return await self.invoke(
            {"@type": "deleteKey", "key": key},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def deleteAllKeys(
        self, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.Ok]:
        """Method for ``deleteAllKeys``"""

        return await self.invoke(
            {
                "@type": "deleteAllKeys",
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def exportKey(
        self,
        input_key: types.InputKey = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.ExportedKey]:
        """Method for ``exportKey``"""

        return await self.invoke(
            {"@type": "exportKey", "input_key": input_key},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def exportPemKey(
        self,
        input_key: types.InputKey = None,
        key_password: bytes = b"",
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.ExportedPemKey]:
        """Method for ``exportPemKey``"""

        return await self.invoke(
            {
                "@type": "exportPemKey",
                "input_key": input_key,
                "key_password": key_password,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def exportEncryptedKey(
        self,
        input_key: types.InputKey = None,
        key_password: bytes = b"",
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.ExportedEncryptedKey]:
        """Method for ``exportEncryptedKey``"""

        return await self.invoke(
            {
                "@type": "exportEncryptedKey",
                "input_key": input_key,
                "key_password": key_password,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def exportUnencryptedKey(
        self,
        input_key: types.InputKey = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.ExportedUnencryptedKey]:
        """Method for ``exportUnencryptedKey``"""

        return await self.invoke(
            {"@type": "exportUnencryptedKey", "input_key": input_key},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def importKey(
        self,
        local_password: bytes = b"",
        mnemonic_password: bytes = b"",
        exported_key: types.ExportedKey = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Key]:
        """Method for ``importKey``"""

        return await self.invoke(
            {
                "@type": "importKey",
                "local_password": local_password,
                "mnemonic_password": mnemonic_password,
                "exported_key": exported_key,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def importPemKey(
        self,
        local_password: bytes = b"",
        key_password: bytes = b"",
        exported_key: types.ExportedPemKey = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Key]:
        """Method for ``importPemKey``"""

        return await self.invoke(
            {
                "@type": "importPemKey",
                "local_password": local_password,
                "key_password": key_password,
                "exported_key": exported_key,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def importEncryptedKey(
        self,
        local_password: bytes = b"",
        key_password: bytes = b"",
        exported_encrypted_key: types.ExportedEncryptedKey = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Key]:
        """Method for ``importEncryptedKey``"""

        return await self.invoke(
            {
                "@type": "importEncryptedKey",
                "local_password": local_password,
                "key_password": key_password,
                "exported_encrypted_key": exported_encrypted_key,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def importUnencryptedKey(
        self,
        local_password: bytes = b"",
        exported_unencrypted_key: types.ExportedUnencryptedKey = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Key]:
        """Method for ``importUnencryptedKey``"""

        return await self.invoke(
            {
                "@type": "importUnencryptedKey",
                "local_password": local_password,
                "exported_unencrypted_key": exported_unencrypted_key,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def changeLocalPassword(
        self,
        input_key: types.InputKey = None,
        new_local_password: bytes = b"",
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Key]:
        """Method for ``changeLocalPassword``"""

        return await self.invoke(
            {
                "@type": "changeLocalPassword",
                "input_key": input_key,
                "new_local_password": new_local_password,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def encrypt(
        self,
        decrypted_data: bytes = b"",
        secret: bytes = b"",
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Data]:
        """Method for ``encrypt``"""

        return await self.invoke(
            {"@type": "encrypt", "decrypted_data": decrypted_data, "secret": secret},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def decrypt(
        self,
        encrypted_data: bytes = b"",
        secret: bytes = b"",
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Data]:
        """Method for ``decrypt``"""

        return await self.invoke(
            {"@type": "decrypt", "encrypted_data": encrypted_data, "secret": secret},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def kdf(
        self,
        password: bytes = b"",
        salt: bytes = b"",
        iterations: int = 0,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Data]:
        """Method for ``kdf``"""

        return await self.invoke(
            {
                "@type": "kdf",
                "password": password,
                "salt": salt,
                "iterations": iterations,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def unpackAccountAddress(
        self,
        account_address: str = "",
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.UnpackedAccountAddress]:
        """Method for ``unpackAccountAddress``"""

        return await self.invoke(
            {"@type": "unpackAccountAddress", "account_address": account_address},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def packAccountAddress(
        self,
        account_address: types.UnpackedAccountAddress = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.AccountAddress]:
        """Method for ``packAccountAddress``"""

        return await self.invoke(
            {"@type": "packAccountAddress", "account_address": account_address},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def getBip39Hints(
        self, prefix: str = "", request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.Bip39Hints]:
        """Method for ``getBip39Hints``"""

        return await self.invoke(
            {"@type": "getBip39Hints", "prefix": prefix},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def rawGetAccountState(
        self,
        account_address: types.AccountAddress = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.RawFullAccountState]:
        """Method for ``raw.getAccountState``"""

        return await self.invoke(
            {"@type": "raw.getAccountState", "account_address": account_address},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def rawGetAccountStateByTransaction(
        self,
        account_address: types.AccountAddress = None,
        transaction_id: types.InternalTransactionId = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.RawFullAccountState]:
        """Method for ``raw.getAccountStateByTransaction``"""

        return await self.invoke(
            {
                "@type": "raw.getAccountStateByTransaction",
                "account_address": account_address,
                "transaction_id": transaction_id,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def rawGetTransactions(
        self,
        private_key: types.InputKey = None,
        account_address: types.AccountAddress = None,
        from_transaction_id: types.InternalTransactionId = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.RawTransactions]:
        """Method for ``raw.getTransactions``"""

        return await self.invoke(
            {
                "@type": "raw.getTransactions",
                "private_key": private_key,
                "account_address": account_address,
                "from_transaction_id": from_transaction_id,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def rawGetTransactionsV2(
        self,
        private_key: types.InputKey = None,
        account_address: types.AccountAddress = None,
        from_transaction_id: types.InternalTransactionId = None,
        count: int = 0,
        try_decode_messages: bool = False,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.RawTransactions]:
        """Method for ``raw.getTransactionsV2``"""

        return await self.invoke(
            {
                "@type": "raw.getTransactionsV2",
                "private_key": private_key,
                "account_address": account_address,
                "from_transaction_id": from_transaction_id,
                "count": count,
                "try_decode_messages": try_decode_messages,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def rawSendMessage(
        self, body: bytes = b"", request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.Ok]:
        """Method for ``raw.sendMessage``"""

        return await self.invoke(
            {"@type": "raw.sendMessage", "body": body},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def rawSendMessageReturnHash(
        self, body: bytes = b"", request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.RawExtMessageInfo]:
        """Method for ``raw.sendMessageReturnHash``"""

        return await self.invoke(
            {"@type": "raw.sendMessageReturnHash", "body": body},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def rawCreateAndSendMessage(
        self,
        destination: types.AccountAddress = None,
        initial_account_state: bytes = b"",
        data: bytes = b"",
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Ok]:
        """Method for ``raw.createAndSendMessage``"""

        return await self.invoke(
            {
                "@type": "raw.createAndSendMessage",
                "destination": destination,
                "initial_account_state": initial_account_state,
                "data": data,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def rawCreateQuery(
        self,
        destination: types.AccountAddress = None,
        init_code: bytes = b"",
        init_data: bytes = b"",
        body: bytes = b"",
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.QueryInfo]:
        """Method for ``raw.createQuery``"""

        return await self.invoke(
            {
                "@type": "raw.createQuery",
                "destination": destination,
                "init_code": init_code,
                "init_data": init_data,
                "body": body,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def sync(
        self, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.TonBlockIdExt]:
        """Method for ``sync``"""

        return await self.invoke(
            {
                "@type": "sync",
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def getAccountAddress(
        self,
        initial_account_state: types.InitialAccountState = None,
        revision: int = 0,
        workchain_id: int = 0,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.AccountAddress]:
        """Method for ``getAccountAddress``"""

        return await self.invoke(
            {
                "@type": "getAccountAddress",
                "initial_account_state": initial_account_state,
                "revision": revision,
                "workchain_id": workchain_id,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def guessAccountRevision(
        self,
        initial_account_state: types.InitialAccountState = None,
        workchain_id: int = 0,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.AccountRevisionList]:
        """Method for ``guessAccountRevision``"""

        return await self.invoke(
            {
                "@type": "guessAccountRevision",
                "initial_account_state": initial_account_state,
                "workchain_id": workchain_id,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def guessAccount(
        self,
        public_key: str = "",
        rwallet_init_public_key: str = "",
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.AccountRevisionList]:
        """Method for ``guessAccount``"""

        return await self.invoke(
            {
                "@type": "guessAccount",
                "public_key": public_key,
                "rwallet_init_public_key": rwallet_init_public_key,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def getAccountState(
        self,
        account_address: types.AccountAddress = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.FullAccountState]:
        """Method for ``getAccountState``"""

        return await self.invoke(
            {"@type": "getAccountState", "account_address": account_address},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def getAccountStateByTransaction(
        self,
        account_address: types.AccountAddress = None,
        transaction_id: types.InternalTransactionId = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.FullAccountState]:
        """Method for ``getAccountStateByTransaction``"""

        return await self.invoke(
            {
                "@type": "getAccountStateByTransaction",
                "account_address": account_address,
                "transaction_id": transaction_id,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def getShardAccountCell(
        self,
        account_address: types.AccountAddress = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.TvmCell]:
        """Method for ``getShardAccountCell``"""

        return await self.invoke(
            {"@type": "getShardAccountCell", "account_address": account_address},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def getShardAccountCellByTransaction(
        self,
        account_address: types.AccountAddress = None,
        transaction_id: types.InternalTransactionId = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.TvmCell]:
        """Method for ``getShardAccountCellByTransaction``"""

        return await self.invoke(
            {
                "@type": "getShardAccountCellByTransaction",
                "account_address": account_address,
                "transaction_id": transaction_id,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def createQuery(
        self,
        private_key: types.InputKey = None,
        address: types.AccountAddress = None,
        timeout: int = 0,
        action: types.Action = None,
        initial_account_state: types.InitialAccountState = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.QueryInfo]:
        """Method for ``createQuery``"""

        return await self.invoke(
            {
                "@type": "createQuery",
                "private_key": private_key,
                "address": address,
                "timeout": timeout,
                "action": action,
                "initial_account_state": initial_account_state,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def getConfigParam(
        self,
        mode: int = 0,
        param: int = 0,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.ConfigInfo]:
        """Method for ``getConfigParam``"""

        return await self.invoke(
            {"@type": "getConfigParam", "mode": mode, "param": param},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def getConfigAll(
        self, mode: int = 0, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.ConfigInfo]:
        """Method for ``getConfigAll``"""

        return await self.invoke(
            {"@type": "getConfigAll", "mode": mode},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def msgDecrypt(
        self,
        input_key: types.InputKey = None,
        data: types.MsgDataEncryptedArray = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.MsgDataDecryptedArray]:
        """Method for ``msg.decrypt``"""

        return await self.invoke(
            {"@type": "msg.decrypt", "input_key": input_key, "data": data},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def msgDecryptWithProof(
        self,
        proof: bytes = b"",
        data: types.MsgDataEncrypted = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.MsgData]:
        """Method for ``msg.decryptWithProof``"""

        return await self.invoke(
            {"@type": "msg.decryptWithProof", "proof": proof, "data": data},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def querySend(
        self, id: int = 0, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.Ok]:
        """Method for ``query.send``"""

        return await self.invoke(
            {"@type": "query.send", "id": id},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def queryForget(
        self, id: int = 0, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.Ok]:
        """Method for ``query.forget``"""

        return await self.invoke(
            {"@type": "query.forget", "id": id},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def queryEstimateFees(
        self,
        id: int = 0,
        ignore_chksig: bool = False,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.QueryFees]:
        """Method for ``query.estimateFees``"""

        return await self.invoke(
            {"@type": "query.estimateFees", "id": id, "ignore_chksig": ignore_chksig},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def queryGetInfo(
        self, id: int = 0, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.QueryInfo]:
        """Method for ``query.getInfo``"""

        return await self.invoke(
            {"@type": "query.getInfo", "id": id},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def smcLoad(
        self,
        account_address: types.AccountAddress = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.SmcInfo]:
        """Method for ``smc.load``"""

        return await self.invoke(
            {"@type": "smc.load", "account_address": account_address},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def smcLoadByTransaction(
        self,
        account_address: types.AccountAddress = None,
        transaction_id: types.InternalTransactionId = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.SmcInfo]:
        """Method for ``smc.loadByTransaction``"""

        return await self.invoke(
            {
                "@type": "smc.loadByTransaction",
                "account_address": account_address,
                "transaction_id": transaction_id,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def smcForget(
        self, id: int = 0, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.Ok]:
        """Method for ``smc.forget``"""

        return await self.invoke(
            {"@type": "smc.forget", "id": id},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def smcGetCode(
        self, id: int = 0, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.TvmCell]:
        """Method for ``smc.getCode``"""

        return await self.invoke(
            {"@type": "smc.getCode", "id": id},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def smcGetData(
        self, id: int = 0, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.TvmCell]:
        """Method for ``smc.getData``"""

        return await self.invoke(
            {"@type": "smc.getData", "id": id},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def smcGetState(
        self, id: int = 0, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.TvmCell]:
        """Method for ``smc.getState``"""

        return await self.invoke(
            {"@type": "smc.getState", "id": id},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def smcRunGetMethod(
        self,
        id: int = 0,
        method: types.SmcMethodId = None,
        stack: List[types.TvmStackEntry] = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.SmcRunResult]:
        """Method for ``smc.runGetMethod``"""

        return await self.invoke(
            {"@type": "smc.runGetMethod", "id": id, "method": method, "stack": stack},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def smcGetLibraries(
        self,
        library_list: List[int] = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.SmcLibraryResult]:
        """Method for ``smc.getLibraries``"""

        return await self.invoke(
            {"@type": "smc.getLibraries", "library_list": library_list},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def smcGetLibrariesExt(
        self,
        list: List[types.SmcLibraryQueryExt] = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.SmcLibraryResultExt]:
        """Method for ``smc.getLibrariesExt``"""

        return await self.invoke(
            {"@type": "smc.getLibrariesExt", "list": list},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def dnsResolve(
        self,
        account_address: types.AccountAddress = None,
        name: str = "",
        category: int = 0,
        ttl: int = 0,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.DnsResolved]:
        """Method for ``dns.resolve``"""

        return await self.invoke(
            {
                "@type": "dns.resolve",
                "account_address": account_address,
                "name": name,
                "category": category,
                "ttl": ttl,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def pchanSignPromise(
        self,
        input_key: types.InputKey = None,
        promise: types.PchanPromise = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.PchanPromise]:
        """Method for ``pchan.signPromise``"""

        return await self.invoke(
            {"@type": "pchan.signPromise", "input_key": input_key, "promise": promise},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def pchanValidatePromise(
        self,
        public_key: bytes = b"",
        promise: types.PchanPromise = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Ok]:
        """Method for ``pchan.validatePromise``"""

        return await self.invoke(
            {
                "@type": "pchan.validatePromise",
                "public_key": public_key,
                "promise": promise,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def pchanPackPromise(
        self,
        promise: types.PchanPromise = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Data]:
        """Method for ``pchan.packPromise``"""

        return await self.invoke(
            {"@type": "pchan.packPromise", "promise": promise},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def pchanUnpackPromise(
        self, data: bytes = b"", request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.PchanPromise]:
        """Method for ``pchan.unpackPromise``"""

        return await self.invoke(
            {"@type": "pchan.unpackPromise", "data": data},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def blocksGetMasterchainInfo(
        self, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.BlocksMasterchainInfo]:
        """Method for ``blocks.getMasterchainInfo``"""

        return await self.invoke(
            {
                "@type": "blocks.getMasterchainInfo",
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def blocksGetShards(
        self,
        id: types.TonBlockIdExt = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.BlocksShards]:
        """Method for ``blocks.getShards``"""

        return await self.invoke(
            {"@type": "blocks.getShards", "id": id},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def blocksLookupBlock(
        self,
        mode: int = 0,
        id: types.TonBlockId = None,
        lt: int = 0,
        utime: int = 0,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.TonBlockIdExt]:
        """Method for ``blocks.lookupBlock``"""

        return await self.invoke(
            {
                "@type": "blocks.lookupBlock",
                "mode": mode,
                "id": id,
                "lt": lt,
                "utime": utime,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def blocksGetTransactions(
        self,
        id: types.TonBlockIdExt = None,
        mode: int = 0,
        count: int = 0,
        after: types.BlocksAccountTransactionId = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.BlocksTransactions]:
        """Method for ``blocks.getTransactions``"""

        return await self.invoke(
            {
                "@type": "blocks.getTransactions",
                "id": id,
                "mode": mode,
                "count": count,
                "after": after,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def blocksGetTransactionsExt(
        self,
        id: types.TonBlockIdExt = None,
        mode: int = 0,
        count: int = 0,
        after: types.BlocksAccountTransactionId = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.BlocksTransactionsExt]:
        """Method for ``blocks.getTransactionsExt``"""

        return await self.invoke(
            {
                "@type": "blocks.getTransactionsExt",
                "id": id,
                "mode": mode,
                "count": count,
                "after": after,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def blocksGetBlockHeader(
        self,
        id: types.TonBlockIdExt = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.BlocksHeader]:
        """Method for ``blocks.getBlockHeader``"""

        return await self.invoke(
            {"@type": "blocks.getBlockHeader", "id": id},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def blocksGetMasterchainBlockSignatures(
        self, seqno: int = 0, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.BlocksBlockSignatures]:
        """Method for ``blocks.getMasterchainBlockSignatures``"""

        return await self.invoke(
            {"@type": "blocks.getMasterchainBlockSignatures", "seqno": seqno},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def blocksGetShardBlockProof(
        self,
        id: types.TonBlockIdExt = None,
        mode: int = 0,
        from_: types.TonBlockIdExt = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.BlocksShardBlockProof]:
        """Method for ``blocks.getShardBlockProof``"""

        return await self.invoke(
            {
                "@type": "blocks.getShardBlockProof",
                "id": id,
                "mode": mode,
                "from_": from_,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def onLiteServerQueryResult(
        self,
        id: int = 0,
        bytes: bytes = b"",
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Ok]:
        """Method for ``onLiteServerQueryResult``"""

        return await self.invoke(
            {"@type": "onLiteServerQueryResult", "id": id, "bytes": bytes},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def onLiteServerQueryError(
        self,
        id: int = 0,
        error: types.Error = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Ok]:
        """Method for ``onLiteServerQueryError``"""

        return await self.invoke(
            {"@type": "onLiteServerQueryError", "id": id, "error": error},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def withBlock(
        self,
        id: types.TonBlockIdExt = None,
        function: dict = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Object]:
        """Method for ``withBlock``"""

        return await self.invoke(
            {"@type": "withBlock", "id": id, "function": function},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def runTests(
        self, dir: str = "", request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.Ok]:
        """Method for ``runTests``"""

        return await self.invoke(
            {"@type": "runTests", "dir": dir},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def liteServerGetInfo(
        self, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.LiteServerInfo]:
        """Method for ``liteServer.getInfo``"""

        return await self.invoke(
            {
                "@type": "liteServer.getInfo",
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def setLogStream(
        self,
        log_stream: types.LogStream = None,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Ok]:
        """Method for ``setLogStream``"""

        return await self.invoke(
            {"@type": "setLogStream", "log_stream": log_stream},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def getLogStream(
        self, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.LogStream]:
        """Method for ``getLogStream``"""

        return await self.invoke(
            {
                "@type": "getLogStream",
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def setLogVerbosityLevel(
        self,
        new_verbosity_level: int = 0,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Ok]:
        """Method for ``setLogVerbosityLevel``"""

        return await self.invoke(
            {
                "@type": "setLogVerbosityLevel",
                "new_verbosity_level": new_verbosity_level,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def getLogVerbosityLevel(
        self, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.LogVerbosityLevel]:
        """Method for ``getLogVerbosityLevel``"""

        return await self.invoke(
            {
                "@type": "getLogVerbosityLevel",
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def getLogTags(
        self, request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.LogTags]:
        """Method for ``getLogTags``"""

        return await self.invoke(
            {
                "@type": "getLogTags",
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def setLogTagVerbosityLevel(
        self,
        tag: str = "",
        new_verbosity_level: int = 0,
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Ok]:
        """Method for ``setLogTagVerbosityLevel``"""

        return await self.invoke(
            {
                "@type": "setLogTagVerbosityLevel",
                "tag": tag,
                "new_verbosity_level": new_verbosity_level,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def getLogTagVerbosityLevel(
        self, tag: str = "", request_timeout: float = 10.0, wait_sync: bool = False
    ) -> Union[types.Error, types.LogVerbosityLevel]:
        """Method for ``getLogTagVerbosityLevel``"""

        return await self.invoke(
            {"@type": "getLogTagVerbosityLevel", "tag": tag},
            timeout=request_timeout,
            wait_sync=wait_sync,
        )

    async def addLogMessage(
        self,
        verbosity_level: int = 0,
        text: str = "",
        request_timeout: float = 10.0,
        wait_sync: bool = False,
    ) -> Union[types.Error, types.Ok]:
        """Method for ``addLogMessage``"""

        return await self.invoke(
            {
                "@type": "addLogMessage",
                "verbosity_level": verbosity_level,
                "text": text,
            },
            timeout=request_timeout,
            wait_sync=wait_sync,
        )
