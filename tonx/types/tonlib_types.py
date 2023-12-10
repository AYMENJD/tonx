from typing import Union, Literal, List
from base64 import b64decode

import tonx


class TlObject:
    """Base class for TL Objects"""

    def getType(self):
        raise NotImplementedError

    def getClass(self):
        raise NotImplementedError

    def to_dict(self) -> dict:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, data: dict):
        raise NotImplementedError


class Error:
    """Class for ``Error``"""

    pass


class Ok:
    """Class for ``Ok``"""

    pass


class KeyStoreType:
    """Class for ``KeyStoreType``"""

    pass


class Config:
    """Class for ``Config``"""

    pass


class Options:
    """Class for ``Options``"""

    pass


class OptionsConfigInfo:
    """Class for ``options.ConfigInfo``"""

    pass


class OptionsInfo:
    """Class for ``options.Info``"""

    pass


class Key:
    """Class for ``Key``"""

    pass


class InputKey:
    """Class for ``InputKey``"""

    pass


class ExportedKey:
    """Class for ``ExportedKey``"""

    pass


class ExportedPemKey:
    """Class for ``ExportedPemKey``"""

    pass


class ExportedEncryptedKey:
    """Class for ``ExportedEncryptedKey``"""

    pass


class ExportedUnencryptedKey:
    """Class for ``ExportedUnencryptedKey``"""

    pass


class Bip39Hints:
    """Class for ``Bip39Hints``"""

    pass


class AdnlAddress:
    """Class for ``AdnlAddress``"""

    pass


class AccountAddress:
    """Class for ``AccountAddress``"""

    pass


class UnpackedAccountAddress:
    """Class for ``UnpackedAccountAddress``"""

    pass


class InternalTransactionId:
    """Class for ``internal.TransactionId``"""

    pass


class InternalBlockId:
    """Class for ``internal.BlockId``"""

    pass


class TonBlockIdExt:
    """Class for ``ton.BlockIdExt``"""

    pass


class RawFullAccountState:
    """Class for ``raw.FullAccountState``"""

    pass


class RawMessage:
    """Class for ``raw.Message``"""

    pass


class RawTransaction:
    """Class for ``raw.Transaction``"""

    pass


class RawTransactions:
    """Class for ``raw.Transactions``"""

    pass


class RawExtMessageInfo:
    """Class for ``raw.ExtMessageInfo``"""

    pass


class PchanConfig:
    """Class for ``pchan.Config``"""

    pass


class InitialAccountState:
    """Class for ``InitialAccountState``"""

    pass


class RwalletLimit:
    """Class for ``rwallet.Limit``"""

    pass


class RwalletConfig:
    """Class for ``rwallet.Config``"""

    pass


class AccountState:
    """Class for ``AccountState``"""

    pass


class PchanState:
    """Class for ``pchan.State``"""

    pass


class FullAccountState:
    """Class for ``FullAccountState``"""

    pass


class AccountRevisionList:
    """Class for ``AccountRevisionList``"""

    pass


class AccountList:
    """Class for ``AccountList``"""

    pass


class SyncState:
    """Class for ``SyncState``"""

    pass


class MsgData:
    """Class for ``msg.Data``"""

    pass


class MsgDataEncrypted:
    """Class for ``msg.DataEncrypted``"""

    pass


class MsgDataDecrypted:
    """Class for ``msg.DataDecrypted``"""

    pass


class MsgDataEncryptedArray:
    """Class for ``msg.DataEncryptedArray``"""

    pass


class MsgDataDecryptedArray:
    """Class for ``msg.DataDecryptedArray``"""

    pass


class MsgMessage:
    """Class for ``msg.Message``"""

    pass


class DnsEntryData:
    """Class for ``dns.EntryData``"""

    pass


class DnsEntry:
    """Class for ``dns.Entry``"""

    pass


class DnsAction:
    """Class for ``dns.Action``"""

    pass


class DnsResolved:
    """Class for ``dns.Resolved``"""

    pass


class PchanPromise:
    """Class for ``pchan.Promise``"""

    pass


class PchanAction:
    """Class for ``pchan.Action``"""

    pass


class RwalletAction:
    """Class for ``rwallet.Action``"""

    pass


class Action:
    """Class for ``Action``"""

    pass


class Fees:
    """Class for ``Fees``"""

    pass


class QueryFees:
    """Class for ``query.Fees``"""

    pass


class QueryInfo:
    """Class for ``query.Info``"""

    pass


class TvmSlice:
    """Class for ``tvm.Slice``"""

    pass


class TvmCell:
    """Class for ``tvm.Cell``"""

    pass


class TvmNumber:
    """Class for ``tvm.Number``"""

    pass


class TvmTuple:
    """Class for ``tvm.Tuple``"""

    pass


class TvmList:
    """Class for ``tvm.List``"""

    pass


class TvmStackEntry:
    """Class for ``tvm.StackEntry``"""

    pass


class SmcInfo:
    """Class for ``smc.Info``"""

    pass


class SmcMethodId:
    """Class for ``smc.MethodId``"""

    pass


class SmcRunResult:
    """Class for ``smc.RunResult``"""

    pass


class SmcLibraryEntry:
    """Class for ``smc.LibraryEntry``"""

    pass


class SmcLibraryResult:
    """Class for ``smc.LibraryResult``"""

    pass


class SmcLibraryQueryExt:
    """Class for ``smc.LibraryQueryExt``"""

    pass


class SmcLibraryResultExt:
    """Class for ``smc.LibraryResultExt``"""

    pass


class Update:
    """Class for ``Update``"""

    pass


class LogStream:
    """Class for ``LogStream``"""

    pass


class LogVerbosityLevel:
    """Class for ``LogVerbosityLevel``"""

    pass


class LogTags:
    """Class for ``LogTags``"""

    pass


class Data:
    """Class for ``Data``"""

    pass


class LiteServerInfo:
    """Class for ``liteServer.Info``"""

    pass


class BlocksMasterchainInfo:
    """Class for ``blocks.MasterchainInfo``"""

    pass


class BlocksShards:
    """Class for ``blocks.Shards``"""

    pass


class BlocksAccountTransactionId:
    """Class for ``blocks.AccountTransactionId``"""

    pass


class LiteServerTransactionId:
    """Class for ``liteServer.TransactionId``"""

    pass


class BlocksTransactions:
    """Class for ``blocks.Transactions``"""

    pass


class BlocksTransactionsExt:
    """Class for ``blocks.TransactionsExt``"""

    pass


class BlocksHeader:
    """Class for ``blocks.Header``"""

    pass


class BlocksSignature:
    """Class for ``blocks.Signature``"""

    pass


class BlocksBlockSignatures:
    """Class for ``blocks.BlockSignatures``"""

    pass


class BlocksShardBlockLink:
    """Class for ``blocks.ShardBlockLink``"""

    pass


class BlocksBlockLinkBack:
    """Class for ``blocks.BlockLinkBack``"""

    pass


class BlocksShardBlockProof:
    """Class for ``blocks.ShardBlockProof``"""

    pass


class ConfigInfo:
    """Class for ``ConfigInfo``"""

    pass


class Object:
    """Class for ``Object``"""

    pass


class Error(TlObject, Error):
    """Type for ``error``"""

    def __init__(self, code: int = 0, message: str = "", extra_id: str = None) -> None:
        self.code: int = int(code)
        self.message: Union[str, None] = message
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["error"]:
        return "error"

    def getClass(self) -> Literal["Error"]:
        return "Error"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "code": self.code,
            "message": self.message,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["Error", None]:
        return (
            cls(
                code=data.get("code", 0),
                message=data.get("message", ""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class Ok(TlObject, Ok):
    """Type for ``ok``"""

    def __init__(self, extra_id: str = None) -> None:
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["ok"]:
        return "ok"

    def getClass(self) -> Literal["Ok"]:
        return "Ok"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["Ok", None]:
        return cls(extra_id=data.get("@extra")) if data else None


class KeyStoreTypeDirectory(TlObject, KeyStoreType):
    """Type for ``keyStoreTypeDirectory``"""

    def __init__(self, directory: str = "", extra_id: str = None) -> None:
        self.directory: Union[str, None] = directory
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["keyStoreTypeDirectory"]:
        return "keyStoreTypeDirectory"

    def getClass(self) -> Literal["KeyStoreType"]:
        return "KeyStoreType"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "directory": self.directory,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["KeyStoreTypeDirectory", None]:
        return (
            cls(directory=data.get("directory", ""), extra_id=data.get("@extra"))
            if data
            else None
        )


class KeyStoreTypeInMemory(TlObject, KeyStoreType):
    """Type for ``keyStoreTypeInMemory``"""

    def __init__(self, extra_id: str = None) -> None:
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["keyStoreTypeInMemory"]:
        return "keyStoreTypeInMemory"

    def getClass(self) -> Literal["KeyStoreType"]:
        return "KeyStoreType"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["KeyStoreTypeInMemory", None]:
        return cls(extra_id=data.get("@extra")) if data else None


class Config(TlObject, Config):
    """Type for ``config``"""

    def __init__(
        self,
        config: str = "",
        blockchain_name: str = "",
        use_callbacks_for_network: bool = False,
        ignore_cache: bool = False,
        extra_id: str = None,
    ) -> None:
        self.config: Union[str, None] = config
        self.blockchain_name: Union[str, None] = blockchain_name
        self.use_callbacks_for_network: bool = bool(use_callbacks_for_network)
        self.ignore_cache: bool = bool(ignore_cache)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["config"]:
        return "config"

    def getClass(self) -> Literal["Config"]:
        return "Config"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "config": self.config,
            "blockchain_name": self.blockchain_name,
            "use_callbacks_for_network": self.use_callbacks_for_network,
            "ignore_cache": self.ignore_cache,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["Config", None]:
        return (
            cls(
                config=data.get("config", ""),
                blockchain_name=data.get("blockchain_name", ""),
                use_callbacks_for_network=data.get("use_callbacks_for_network", False),
                ignore_cache=data.get("ignore_cache", False),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class Options(TlObject, Options):
    """Type for ``options``"""

    def __init__(
        self,
        config: Config = None,
        keystore_type: KeyStoreType = None,
        extra_id: str = None,
    ) -> None:
        self.config: Union[Config, None] = config
        self.keystore_type: Union[
            KeyStoreTypeDirectory, KeyStoreTypeInMemory, None
        ] = keystore_type
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["options"]:
        return "options"

    def getClass(self) -> Literal["Options"]:
        return "Options"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "config": self.config,
            "keystore_type": self.keystore_type,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["Options", None]:
        return (
            cls(
                config=data.get("config", None),
                keystore_type=data.get("keystore_type", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class OptionsConfigInfo(TlObject, OptionsConfigInfo):
    """Type for ``options.configInfo``"""

    def __init__(
        self,
        default_wallet_id: int = 0,
        default_rwallet_init_public_key: str = "",
        extra_id: str = None,
    ) -> None:
        self.default_wallet_id: int = int(default_wallet_id)
        self.default_rwallet_init_public_key: Union[
            str, None
        ] = default_rwallet_init_public_key
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["options.configInfo"]:
        return "options.configInfo"

    def getClass(self) -> Literal["options.ConfigInfo"]:
        return "options.ConfigInfo"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "default_wallet_id": self.default_wallet_id,
            "default_rwallet_init_public_key": self.default_rwallet_init_public_key,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["OptionsConfigInfo", None]:
        return (
            cls(
                default_wallet_id=data.get("default_wallet_id", 0),
                default_rwallet_init_public_key=data.get(
                    "default_rwallet_init_public_key", ""
                ),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class OptionsInfo(TlObject, OptionsInfo):
    """Type for ``options.info``"""

    def __init__(
        self, config_info: OptionsConfigInfo = None, extra_id: str = None
    ) -> None:
        self.config_info: Union[OptionsConfigInfo, None] = config_info
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["options.info"]:
        return "options.info"

    def getClass(self) -> Literal["options.Info"]:
        return "options.Info"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "config_info": self.config_info,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["OptionsInfo", None]:
        return (
            cls(config_info=data.get("config_info", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class Key(TlObject, Key):
    """Type for ``key``"""

    def __init__(
        self, public_key: str = "", secret: bytes = b"", extra_id: str = None
    ) -> None:
        self.public_key: Union[str, None] = public_key
        self.secret: bytes = b64decode(secret)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["key"]:
        return "key"

    def getClass(self) -> Literal["Key"]:
        return "Key"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "public_key": self.public_key,
            "secret": self.secret,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["Key", None]:
        return (
            cls(
                public_key=data.get("public_key", ""),
                secret=data.get("secret", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class InputKeyRegular(TlObject, InputKey):
    """Type for ``inputKeyRegular``"""

    def __init__(
        self, key: Key = None, local_password: bytes = b"", extra_id: str = None
    ) -> None:
        self.key: Union[Key, None] = key
        self.local_password: bytes = b64decode(local_password)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["inputKeyRegular"]:
        return "inputKeyRegular"

    def getClass(self) -> Literal["InputKey"]:
        return "InputKey"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "key": self.key,
            "local_password": self.local_password,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["InputKeyRegular", None]:
        return (
            cls(
                key=data.get("key", None),
                local_password=data.get("local_password", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class InputKeyFake(TlObject, InputKey):
    """Type for ``inputKeyFake``"""

    def __init__(self, extra_id: str = None) -> None:
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["inputKeyFake"]:
        return "inputKeyFake"

    def getClass(self) -> Literal["InputKey"]:
        return "InputKey"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["InputKeyFake", None]:
        return cls(extra_id=data.get("@extra")) if data else None


class ExportedKey(TlObject, ExportedKey):
    """Type for ``exportedKey``"""

    def __init__(self, word_list: List[str] = None, extra_id: str = None) -> None:
        self.word_list: List[str] = word_list or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["exportedKey"]:
        return "exportedKey"

    def getClass(self) -> Literal["ExportedKey"]:
        return "ExportedKey"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "word_list": self.word_list,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["ExportedKey", None]:
        return (
            cls(word_list=data.get("word_list", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class ExportedPemKey(TlObject, ExportedPemKey):
    """Type for ``exportedPemKey``"""

    def __init__(self, pem: str = "", extra_id: str = None) -> None:
        self.pem: Union[str, None] = pem
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["exportedPemKey"]:
        return "exportedPemKey"

    def getClass(self) -> Literal["ExportedPemKey"]:
        return "ExportedPemKey"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "pem": self.pem, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["ExportedPemKey", None]:
        return (
            cls(pem=data.get("pem", ""), extra_id=data.get("@extra")) if data else None
        )


class ExportedEncryptedKey(TlObject, ExportedEncryptedKey):
    """Type for ``exportedEncryptedKey``"""

    def __init__(self, data: bytes = b"", extra_id: str = None) -> None:
        self.data: bytes = b64decode(data)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["exportedEncryptedKey"]:
        return "exportedEncryptedKey"

    def getClass(self) -> Literal["ExportedEncryptedKey"]:
        return "ExportedEncryptedKey"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "data": self.data, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["ExportedEncryptedKey", None]:
        return (
            cls(data=data.get("data", b""), extra_id=data.get("@extra"))
            if data
            else None
        )


class ExportedUnencryptedKey(TlObject, ExportedUnencryptedKey):
    """Type for ``exportedUnencryptedKey``"""

    def __init__(self, data: bytes = b"", extra_id: str = None) -> None:
        self.data: bytes = b64decode(data)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["exportedUnencryptedKey"]:
        return "exportedUnencryptedKey"

    def getClass(self) -> Literal["ExportedUnencryptedKey"]:
        return "ExportedUnencryptedKey"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "data": self.data, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["ExportedUnencryptedKey", None]:
        return (
            cls(data=data.get("data", b""), extra_id=data.get("@extra"))
            if data
            else None
        )


class Bip39Hints(TlObject, Bip39Hints):
    """Type for ``bip39Hints``"""

    def __init__(self, words: List[str] = None, extra_id: str = None) -> None:
        self.words: List[str] = words or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["bip39Hints"]:
        return "bip39Hints"

    def getClass(self) -> Literal["Bip39Hints"]:
        return "Bip39Hints"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "words": self.words, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["Bip39Hints", None]:
        return (
            cls(words=data.get("words", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class AdnlAddress(TlObject, AdnlAddress):
    """Type for ``adnlAddress``"""

    def __init__(self, adnl_address: str = "", extra_id: str = None) -> None:
        self.adnl_address: Union[str, None] = adnl_address
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["adnlAddress"]:
        return "adnlAddress"

    def getClass(self) -> Literal["AdnlAddress"]:
        return "AdnlAddress"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "adnl_address": self.adnl_address,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["AdnlAddress", None]:
        return (
            cls(adnl_address=data.get("adnl_address", ""), extra_id=data.get("@extra"))
            if data
            else None
        )


class AccountAddress(TlObject, AccountAddress):
    """Type for ``accountAddress``"""

    def __init__(self, account_address: str = "", extra_id: str = None) -> None:
        self.account_address: Union[str, None] = account_address
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["accountAddress"]:
        return "accountAddress"

    def getClass(self) -> Literal["AccountAddress"]:
        return "AccountAddress"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "account_address": self.account_address,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["AccountAddress", None]:
        return (
            cls(
                account_address=data.get("account_address", ""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class UnpackedAccountAddress(TlObject, UnpackedAccountAddress):
    """Type for ``unpackedAccountAddress``"""

    def __init__(
        self,
        workchain_id: int = 0,
        bounceable: bool = False,
        testnet: bool = False,
        addr: bytes = b"",
        extra_id: str = None,
    ) -> None:
        self.workchain_id: int = int(workchain_id)
        self.bounceable: bool = bool(bounceable)
        self.testnet: bool = bool(testnet)
        self.addr: bytes = b64decode(addr)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["unpackedAccountAddress"]:
        return "unpackedAccountAddress"

    def getClass(self) -> Literal["UnpackedAccountAddress"]:
        return "UnpackedAccountAddress"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "workchain_id": self.workchain_id,
            "bounceable": self.bounceable,
            "testnet": self.testnet,
            "addr": self.addr,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["UnpackedAccountAddress", None]:
        return (
            cls(
                workchain_id=data.get("workchain_id", 0),
                bounceable=data.get("bounceable", False),
                testnet=data.get("testnet", False),
                addr=data.get("addr", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class InternalTransactionId(TlObject, InternalTransactionId):
    """Type for ``internal.transactionId``"""

    def __init__(self, lt: int = 0, hash: bytes = b"", extra_id: str = None) -> None:
        self.lt: int = int(lt)
        self.hash: bytes = b64decode(hash)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["internal.transactionId"]:
        return "internal.transactionId"

    def getClass(self) -> Literal["internal.TransactionId"]:
        return "internal.TransactionId"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "lt": self.lt,
            "hash": self.hash,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["InternalTransactionId", None]:
        return (
            cls(
                lt=data.get("lt", 0),
                hash=data.get("hash", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class TonBlockId(TlObject, InternalBlockId):
    """Type for ``ton.blockId``"""

    def __init__(
        self, workchain: int = 0, shard: int = 0, seqno: int = 0, extra_id: str = None
    ) -> None:
        self.workchain: int = int(workchain)
        self.shard: int = int(shard)
        self.seqno: int = int(seqno)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["ton.blockId"]:
        return "ton.blockId"

    def getClass(self) -> Literal["internal.BlockId"]:
        return "internal.BlockId"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "workchain": self.workchain,
            "shard": self.shard,
            "seqno": self.seqno,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TonBlockId", None]:
        return (
            cls(
                workchain=data.get("workchain", 0),
                shard=data.get("shard", 0),
                seqno=data.get("seqno", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class TonBlockIdExt(TlObject, TonBlockIdExt):
    """Type for ``ton.blockIdExt``"""

    def __init__(
        self,
        workchain: int = 0,
        shard: int = 0,
        seqno: int = 0,
        root_hash: bytes = b"",
        file_hash: bytes = b"",
        extra_id: str = None,
    ) -> None:
        self.workchain: int = int(workchain)
        self.shard: int = int(shard)
        self.seqno: int = int(seqno)
        self.root_hash: bytes = b64decode(root_hash)
        self.file_hash: bytes = b64decode(file_hash)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["ton.blockIdExt"]:
        return "ton.blockIdExt"

    def getClass(self) -> Literal["ton.BlockIdExt"]:
        return "ton.BlockIdExt"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "workchain": self.workchain,
            "shard": self.shard,
            "seqno": self.seqno,
            "root_hash": self.root_hash,
            "file_hash": self.file_hash,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TonBlockIdExt", None]:
        return (
            cls(
                workchain=data.get("workchain", 0),
                shard=data.get("shard", 0),
                seqno=data.get("seqno", 0),
                root_hash=data.get("root_hash", b""),
                file_hash=data.get("file_hash", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class RawFullAccountState(TlObject, RawFullAccountState):
    """Type for ``raw.fullAccountState``"""

    def __init__(
        self,
        balance: int = 0,
        code: bytes = b"",
        data: bytes = b"",
        last_transaction_id: InternalTransactionId = None,
        block_id: TonBlockIdExt = None,
        frozen_hash: bytes = b"",
        sync_utime: int = 0,
        extra_id: str = None,
    ) -> None:
        self.balance: int = int(balance)
        self.code: bytes = b64decode(code)
        self.data: bytes = b64decode(data)
        self.last_transaction_id: Union[
            InternalTransactionId, None
        ] = last_transaction_id
        self.block_id: Union[TonBlockIdExt, None] = block_id
        self.frozen_hash: bytes = b64decode(frozen_hash)
        self.sync_utime: int = int(sync_utime)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["raw.fullAccountState"]:
        return "raw.fullAccountState"

    def getClass(self) -> Literal["raw.FullAccountState"]:
        return "raw.FullAccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "balance": self.balance,
            "code": self.code,
            "data": self.data,
            "last_transaction_id": self.last_transaction_id,
            "block_id": self.block_id,
            "frozen_hash": self.frozen_hash,
            "sync_utime": self.sync_utime,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["RawFullAccountState", None]:
        return (
            cls(
                balance=data.get("balance", 0),
                code=data.get("code", b""),
                data=data.get("data", b""),
                last_transaction_id=data.get("last_transaction_id", None),
                block_id=data.get("block_id", None),
                frozen_hash=data.get("frozen_hash", b""),
                sync_utime=data.get("sync_utime", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class RawMessage(TlObject, RawMessage):
    """Type for ``raw.message``"""

    def __init__(
        self,
        source: AccountAddress = None,
        destination: AccountAddress = None,
        value: int = 0,
        fwd_fee: int = 0,
        ihr_fee: int = 0,
        created_lt: int = 0,
        body_hash: bytes = b"",
        msg_data: MsgData = None,
        extra_id: str = None,
    ) -> None:
        self.source: Union[AccountAddress, None] = source
        self.destination: Union[AccountAddress, None] = destination
        self.value: int = int(value)
        self.fwd_fee: int = int(fwd_fee)
        self.ihr_fee: int = int(ihr_fee)
        self.created_lt: int = int(created_lt)
        self.body_hash: bytes = b64decode(body_hash)
        self.msg_data: Union[
            MsgDataRaw, MsgDataText, MsgDataDecryptedText, MsgDataEncryptedText, None
        ] = msg_data
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["raw.message"]:
        return "raw.message"

    def getClass(self) -> Literal["raw.Message"]:
        return "raw.Message"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "source": self.source,
            "destination": self.destination,
            "value": self.value,
            "fwd_fee": self.fwd_fee,
            "ihr_fee": self.ihr_fee,
            "created_lt": self.created_lt,
            "body_hash": self.body_hash,
            "msg_data": self.msg_data,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["RawMessage", None]:
        return (
            cls(
                source=data.get("source", None),
                destination=data.get("destination", None),
                value=data.get("value", 0),
                fwd_fee=data.get("fwd_fee", 0),
                ihr_fee=data.get("ihr_fee", 0),
                created_lt=data.get("created_lt", 0),
                body_hash=data.get("body_hash", b""),
                msg_data=data.get("msg_data", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class RawTransaction(TlObject, RawTransaction):
    """Type for ``raw.transaction``"""

    def __init__(
        self,
        address: AccountAddress = None,
        utime: int = 0,
        data: bytes = b"",
        transaction_id: InternalTransactionId = None,
        fee: int = 0,
        storage_fee: int = 0,
        other_fee: int = 0,
        in_msg: RawMessage = None,
        out_msgs: List[RawMessage] = None,
        extra_id: str = None,
    ) -> None:
        self.address: Union[AccountAddress, None] = address
        self.utime: int = int(utime)
        self.data: bytes = b64decode(data)
        self.transaction_id: Union[InternalTransactionId, None] = transaction_id
        self.fee: int = int(fee)
        self.storage_fee: int = int(storage_fee)
        self.other_fee: int = int(other_fee)
        self.in_msg: Union[RawMessage, None] = in_msg
        self.out_msgs: List[RawMessage] = out_msgs or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["raw.transaction"]:
        return "raw.transaction"

    def getClass(self) -> Literal["raw.Transaction"]:
        return "raw.Transaction"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "address": self.address,
            "utime": self.utime,
            "data": self.data,
            "transaction_id": self.transaction_id,
            "fee": self.fee,
            "storage_fee": self.storage_fee,
            "other_fee": self.other_fee,
            "in_msg": self.in_msg,
            "out_msgs": self.out_msgs,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["RawTransaction", None]:
        return (
            cls(
                address=data.get("address", None),
                utime=data.get("utime", 0),
                data=data.get("data", b""),
                transaction_id=data.get("transaction_id", None),
                fee=data.get("fee", 0),
                storage_fee=data.get("storage_fee", 0),
                other_fee=data.get("other_fee", 0),
                in_msg=data.get("in_msg", None),
                out_msgs=data.get("out_msgs", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class RawTransactions(TlObject, RawTransactions):
    """Type for ``raw.transactions``"""

    def __init__(
        self,
        transactions: List[RawTransaction] = None,
        previous_transaction_id: InternalTransactionId = None,
        extra_id: str = None,
    ) -> None:
        self.transactions: List[RawTransaction] = transactions or []
        self.previous_transaction_id: Union[
            InternalTransactionId, None
        ] = previous_transaction_id
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["raw.transactions"]:
        return "raw.transactions"

    def getClass(self) -> Literal["raw.Transactions"]:
        return "raw.Transactions"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "transactions": self.transactions,
            "previous_transaction_id": self.previous_transaction_id,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["RawTransactions", None]:
        return (
            cls(
                transactions=data.get("transactions", None),
                previous_transaction_id=data.get("previous_transaction_id", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class RawExtMessageInfo(TlObject, RawExtMessageInfo):
    """Type for ``raw.extMessageInfo``"""

    def __init__(self, hash: bytes = b"", extra_id: str = None) -> None:
        self.hash: bytes = b64decode(hash)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["raw.extMessageInfo"]:
        return "raw.extMessageInfo"

    def getClass(self) -> Literal["raw.ExtMessageInfo"]:
        return "raw.ExtMessageInfo"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "hash": self.hash, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["RawExtMessageInfo", None]:
        return (
            cls(hash=data.get("hash", b""), extra_id=data.get("@extra"))
            if data
            else None
        )


class PchanConfig(TlObject, PchanConfig):
    """Type for ``pchan.config``"""

    def __init__(
        self,
        alice_public_key: str = "",
        alice_address: AccountAddress = None,
        bob_public_key: str = "",
        bob_address: AccountAddress = None,
        init_timeout: int = 0,
        close_timeout: int = 0,
        channel_id: int = 0,
        extra_id: str = None,
    ) -> None:
        self.alice_public_key: Union[str, None] = alice_public_key
        self.alice_address: Union[AccountAddress, None] = alice_address
        self.bob_public_key: Union[str, None] = bob_public_key
        self.bob_address: Union[AccountAddress, None] = bob_address
        self.init_timeout: int = int(init_timeout)
        self.close_timeout: int = int(close_timeout)
        self.channel_id: int = int(channel_id)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["pchan.config"]:
        return "pchan.config"

    def getClass(self) -> Literal["pchan.Config"]:
        return "pchan.Config"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "alice_public_key": self.alice_public_key,
            "alice_address": self.alice_address,
            "bob_public_key": self.bob_public_key,
            "bob_address": self.bob_address,
            "init_timeout": self.init_timeout,
            "close_timeout": self.close_timeout,
            "channel_id": self.channel_id,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["PchanConfig", None]:
        return (
            cls(
                alice_public_key=data.get("alice_public_key", ""),
                alice_address=data.get("alice_address", None),
                bob_public_key=data.get("bob_public_key", ""),
                bob_address=data.get("bob_address", None),
                init_timeout=data.get("init_timeout", 0),
                close_timeout=data.get("close_timeout", 0),
                channel_id=data.get("channel_id", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class RawInitialAccountState(TlObject, InitialAccountState):
    """Type for ``raw.initialAccountState``"""

    def __init__(
        self, code: bytes = b"", data: bytes = b"", extra_id: str = None
    ) -> None:
        self.code: bytes = b64decode(code)
        self.data: bytes = b64decode(data)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["raw.initialAccountState"]:
        return "raw.initialAccountState"

    def getClass(self) -> Literal["InitialAccountState"]:
        return "InitialAccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "code": self.code,
            "data": self.data,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["RawInitialAccountState", None]:
        return (
            cls(
                code=data.get("code", b""),
                data=data.get("data", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class WalletV3InitialAccountState(TlObject, InitialAccountState):
    """Type for ``wallet.v3.initialAccountState``"""

    def __init__(
        self, public_key: str = "", wallet_id: int = 0, extra_id: str = None
    ) -> None:
        self.public_key: Union[str, None] = public_key
        self.wallet_id: int = int(wallet_id)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["wallet.v3.initialAccountState"]:
        return "wallet.v3.initialAccountState"

    def getClass(self) -> Literal["InitialAccountState"]:
        return "InitialAccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "public_key": self.public_key,
            "wallet_id": self.wallet_id,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["WalletV3InitialAccountState", None]:
        return (
            cls(
                public_key=data.get("public_key", ""),
                wallet_id=data.get("wallet_id", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class WalletV4InitialAccountState(TlObject, InitialAccountState):
    """Type for ``wallet.v4.initialAccountState``"""

    def __init__(
        self, public_key: str = "", wallet_id: int = 0, extra_id: str = None
    ) -> None:
        self.public_key: Union[str, None] = public_key
        self.wallet_id: int = int(wallet_id)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["wallet.v4.initialAccountState"]:
        return "wallet.v4.initialAccountState"

    def getClass(self) -> Literal["InitialAccountState"]:
        return "InitialAccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "public_key": self.public_key,
            "wallet_id": self.wallet_id,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["WalletV4InitialAccountState", None]:
        return (
            cls(
                public_key=data.get("public_key", ""),
                wallet_id=data.get("wallet_id", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class WalletHighloadV1InitialAccountState(TlObject, InitialAccountState):
    """Type for ``wallet.highload.v1.initialAccountState``"""

    def __init__(
        self, public_key: str = "", wallet_id: int = 0, extra_id: str = None
    ) -> None:
        self.public_key: Union[str, None] = public_key
        self.wallet_id: int = int(wallet_id)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["wallet.highload.v1.initialAccountState"]:
        return "wallet.highload.v1.initialAccountState"

    def getClass(self) -> Literal["InitialAccountState"]:
        return "InitialAccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "public_key": self.public_key,
            "wallet_id": self.wallet_id,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(
        cls, data: dict
    ) -> Union["WalletHighloadV1InitialAccountState", None]:
        return (
            cls(
                public_key=data.get("public_key", ""),
                wallet_id=data.get("wallet_id", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class WalletHighloadV2InitialAccountState(TlObject, InitialAccountState):
    """Type for ``wallet.highload.v2.initialAccountState``"""

    def __init__(
        self, public_key: str = "", wallet_id: int = 0, extra_id: str = None
    ) -> None:
        self.public_key: Union[str, None] = public_key
        self.wallet_id: int = int(wallet_id)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["wallet.highload.v2.initialAccountState"]:
        return "wallet.highload.v2.initialAccountState"

    def getClass(self) -> Literal["InitialAccountState"]:
        return "InitialAccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "public_key": self.public_key,
            "wallet_id": self.wallet_id,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(
        cls, data: dict
    ) -> Union["WalletHighloadV2InitialAccountState", None]:
        return (
            cls(
                public_key=data.get("public_key", ""),
                wallet_id=data.get("wallet_id", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class RwalletLimit(TlObject, RwalletLimit):
    """Type for ``rwallet.limit``"""

    def __init__(self, seconds: int = 0, value: int = 0, extra_id: str = None) -> None:
        self.seconds: int = int(seconds)
        self.value: int = int(value)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["rwallet.limit"]:
        return "rwallet.limit"

    def getClass(self) -> Literal["rwallet.Limit"]:
        return "rwallet.Limit"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "seconds": self.seconds,
            "value": self.value,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["RwalletLimit", None]:
        return (
            cls(
                seconds=data.get("seconds", 0),
                value=data.get("value", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class RwalletConfig(TlObject, RwalletConfig):
    """Type for ``rwallet.config``"""

    def __init__(
        self, start_at: int = 0, limits: List[RwalletLimit] = None, extra_id: str = None
    ) -> None:
        self.start_at: int = int(start_at)
        self.limits: List[RwalletLimit] = limits or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["rwallet.config"]:
        return "rwallet.config"

    def getClass(self) -> Literal["rwallet.Config"]:
        return "rwallet.Config"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "start_at": self.start_at,
            "limits": self.limits,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["RwalletConfig", None]:
        return (
            cls(
                start_at=data.get("start_at", 0),
                limits=data.get("limits", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class RwalletInitialAccountState(TlObject, InitialAccountState):
    """Type for ``rwallet.initialAccountState``"""

    def __init__(
        self,
        init_public_key: str = "",
        public_key: str = "",
        wallet_id: int = 0,
        extra_id: str = None,
    ) -> None:
        self.init_public_key: Union[str, None] = init_public_key
        self.public_key: Union[str, None] = public_key
        self.wallet_id: int = int(wallet_id)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["rwallet.initialAccountState"]:
        return "rwallet.initialAccountState"

    def getClass(self) -> Literal["InitialAccountState"]:
        return "InitialAccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "init_public_key": self.init_public_key,
            "public_key": self.public_key,
            "wallet_id": self.wallet_id,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["RwalletInitialAccountState", None]:
        return (
            cls(
                init_public_key=data.get("init_public_key", ""),
                public_key=data.get("public_key", ""),
                wallet_id=data.get("wallet_id", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class DnsInitialAccountState(TlObject, InitialAccountState):
    """Type for ``dns.initialAccountState``"""

    def __init__(
        self, public_key: str = "", wallet_id: int = 0, extra_id: str = None
    ) -> None:
        self.public_key: Union[str, None] = public_key
        self.wallet_id: int = int(wallet_id)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.initialAccountState"]:
        return "dns.initialAccountState"

    def getClass(self) -> Literal["InitialAccountState"]:
        return "InitialAccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "public_key": self.public_key,
            "wallet_id": self.wallet_id,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsInitialAccountState", None]:
        return (
            cls(
                public_key=data.get("public_key", ""),
                wallet_id=data.get("wallet_id", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class PchanInitialAccountState(TlObject, InitialAccountState):
    """Type for ``pchan.initialAccountState``"""

    def __init__(self, config: PchanConfig = None, extra_id: str = None) -> None:
        self.config: Union[PchanConfig, None] = config
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["pchan.initialAccountState"]:
        return "pchan.initialAccountState"

    def getClass(self) -> Literal["InitialAccountState"]:
        return "InitialAccountState"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "config": self.config, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["PchanInitialAccountState", None]:
        return (
            cls(config=data.get("config", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class RawAccountState(TlObject, AccountState):
    """Type for ``raw.accountState``"""

    def __init__(
        self,
        code: bytes = b"",
        data: bytes = b"",
        frozen_hash: bytes = b"",
        extra_id: str = None,
    ) -> None:
        self.code: bytes = b64decode(code)
        self.data: bytes = b64decode(data)
        self.frozen_hash: bytes = b64decode(frozen_hash)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["raw.accountState"]:
        return "raw.accountState"

    def getClass(self) -> Literal["AccountState"]:
        return "AccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "code": self.code,
            "data": self.data,
            "frozen_hash": self.frozen_hash,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["RawAccountState", None]:
        return (
            cls(
                code=data.get("code", b""),
                data=data.get("data", b""),
                frozen_hash=data.get("frozen_hash", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class WalletV3AccountState(TlObject, AccountState):
    """Type for ``wallet.v3.accountState``"""

    def __init__(
        self, wallet_id: int = 0, seqno: int = 0, extra_id: str = None
    ) -> None:
        self.wallet_id: int = int(wallet_id)
        self.seqno: int = int(seqno)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["wallet.v3.accountState"]:
        return "wallet.v3.accountState"

    def getClass(self) -> Literal["AccountState"]:
        return "AccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "wallet_id": self.wallet_id,
            "seqno": self.seqno,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["WalletV3AccountState", None]:
        return (
            cls(
                wallet_id=data.get("wallet_id", 0),
                seqno=data.get("seqno", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class WalletV4AccountState(TlObject, AccountState):
    """Type for ``wallet.v4.accountState``"""

    def __init__(
        self, wallet_id: int = 0, seqno: int = 0, extra_id: str = None
    ) -> None:
        self.wallet_id: int = int(wallet_id)
        self.seqno: int = int(seqno)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["wallet.v4.accountState"]:
        return "wallet.v4.accountState"

    def getClass(self) -> Literal["AccountState"]:
        return "AccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "wallet_id": self.wallet_id,
            "seqno": self.seqno,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["WalletV4AccountState", None]:
        return (
            cls(
                wallet_id=data.get("wallet_id", 0),
                seqno=data.get("seqno", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class WalletHighloadV1AccountState(TlObject, AccountState):
    """Type for ``wallet.highload.v1.accountState``"""

    def __init__(
        self, wallet_id: int = 0, seqno: int = 0, extra_id: str = None
    ) -> None:
        self.wallet_id: int = int(wallet_id)
        self.seqno: int = int(seqno)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["wallet.highload.v1.accountState"]:
        return "wallet.highload.v1.accountState"

    def getClass(self) -> Literal["AccountState"]:
        return "AccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "wallet_id": self.wallet_id,
            "seqno": self.seqno,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["WalletHighloadV1AccountState", None]:
        return (
            cls(
                wallet_id=data.get("wallet_id", 0),
                seqno=data.get("seqno", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class WalletHighloadV2AccountState(TlObject, AccountState):
    """Type for ``wallet.highload.v2.accountState``"""

    def __init__(self, wallet_id: int = 0, extra_id: str = None) -> None:
        self.wallet_id: int = int(wallet_id)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["wallet.highload.v2.accountState"]:
        return "wallet.highload.v2.accountState"

    def getClass(self) -> Literal["AccountState"]:
        return "AccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "wallet_id": self.wallet_id,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["WalletHighloadV2AccountState", None]:
        return (
            cls(wallet_id=data.get("wallet_id", 0), extra_id=data.get("@extra"))
            if data
            else None
        )


class DnsAccountState(TlObject, AccountState):
    """Type for ``dns.accountState``"""

    def __init__(self, wallet_id: int = 0, extra_id: str = None) -> None:
        self.wallet_id: int = int(wallet_id)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.accountState"]:
        return "dns.accountState"

    def getClass(self) -> Literal["AccountState"]:
        return "AccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "wallet_id": self.wallet_id,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsAccountState", None]:
        return (
            cls(wallet_id=data.get("wallet_id", 0), extra_id=data.get("@extra"))
            if data
            else None
        )


class RwalletAccountState(TlObject, AccountState):
    """Type for ``rwallet.accountState``"""

    def __init__(
        self,
        wallet_id: int = 0,
        seqno: int = 0,
        unlocked_balance: int = 0,
        config: RwalletConfig = None,
        extra_id: str = None,
    ) -> None:
        self.wallet_id: int = int(wallet_id)
        self.seqno: int = int(seqno)
        self.unlocked_balance: int = int(unlocked_balance)
        self.config: Union[RwalletConfig, None] = config
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["rwallet.accountState"]:
        return "rwallet.accountState"

    def getClass(self) -> Literal["AccountState"]:
        return "AccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "wallet_id": self.wallet_id,
            "seqno": self.seqno,
            "unlocked_balance": self.unlocked_balance,
            "config": self.config,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["RwalletAccountState", None]:
        return (
            cls(
                wallet_id=data.get("wallet_id", 0),
                seqno=data.get("seqno", 0),
                unlocked_balance=data.get("unlocked_balance", 0),
                config=data.get("config", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class PchanStateInit(TlObject, PchanState):
    """Type for ``pchan.stateInit``"""

    def __init__(
        self,
        signed_A: bool = False,
        signed_B: bool = False,
        min_A: int = 0,
        min_B: int = 0,
        expire_at: int = 0,
        A: int = 0,
        B: int = 0,
        extra_id: str = None,
    ) -> None:
        self.signed_A: bool = bool(signed_A)
        self.signed_B: bool = bool(signed_B)
        self.min_A: int = int(min_A)
        self.min_B: int = int(min_B)
        self.expire_at: int = int(expire_at)
        self.A: int = int(A)
        self.B: int = int(B)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["pchan.stateInit"]:
        return "pchan.stateInit"

    def getClass(self) -> Literal["pchan.State"]:
        return "pchan.State"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "signed_A": self.signed_A,
            "signed_B": self.signed_B,
            "min_A": self.min_A,
            "min_B": self.min_B,
            "expire_at": self.expire_at,
            "A": self.A,
            "B": self.B,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["PchanStateInit", None]:
        return (
            cls(
                signed_A=data.get("signed_A", False),
                signed_B=data.get("signed_B", False),
                min_A=data.get("min_A", 0),
                min_B=data.get("min_B", 0),
                expire_at=data.get("expire_at", 0),
                A=data.get("A", 0),
                B=data.get("B", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class PchanStateClose(TlObject, PchanState):
    """Type for ``pchan.stateClose``"""

    def __init__(
        self,
        signed_A: bool = False,
        signed_B: bool = False,
        min_A: int = 0,
        min_B: int = 0,
        expire_at: int = 0,
        A: int = 0,
        B: int = 0,
        extra_id: str = None,
    ) -> None:
        self.signed_A: bool = bool(signed_A)
        self.signed_B: bool = bool(signed_B)
        self.min_A: int = int(min_A)
        self.min_B: int = int(min_B)
        self.expire_at: int = int(expire_at)
        self.A: int = int(A)
        self.B: int = int(B)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["pchan.stateClose"]:
        return "pchan.stateClose"

    def getClass(self) -> Literal["pchan.State"]:
        return "pchan.State"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "signed_A": self.signed_A,
            "signed_B": self.signed_B,
            "min_A": self.min_A,
            "min_B": self.min_B,
            "expire_at": self.expire_at,
            "A": self.A,
            "B": self.B,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["PchanStateClose", None]:
        return (
            cls(
                signed_A=data.get("signed_A", False),
                signed_B=data.get("signed_B", False),
                min_A=data.get("min_A", 0),
                min_B=data.get("min_B", 0),
                expire_at=data.get("expire_at", 0),
                A=data.get("A", 0),
                B=data.get("B", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class PchanStatePayout(TlObject, PchanState):
    """Type for ``pchan.statePayout``"""

    def __init__(self, A: int = 0, B: int = 0, extra_id: str = None) -> None:
        self.A: int = int(A)
        self.B: int = int(B)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["pchan.statePayout"]:
        return "pchan.statePayout"

    def getClass(self) -> Literal["pchan.State"]:
        return "pchan.State"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "A": self.A,
            "B": self.B,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["PchanStatePayout", None]:
        return (
            cls(A=data.get("A", 0), B=data.get("B", 0), extra_id=data.get("@extra"))
            if data
            else None
        )


class PchanAccountState(TlObject, AccountState):
    """Type for ``pchan.accountState``"""

    def __init__(
        self,
        config: PchanConfig = None,
        state: PchanState = None,
        description: str = "",
        extra_id: str = None,
    ) -> None:
        self.config: Union[PchanConfig, None] = config
        self.state: Union[
            PchanStateInit, PchanStateClose, PchanStatePayout, None
        ] = state
        self.description: Union[str, None] = description
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["pchan.accountState"]:
        return "pchan.accountState"

    def getClass(self) -> Literal["AccountState"]:
        return "AccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "config": self.config,
            "state": self.state,
            "description": self.description,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["PchanAccountState", None]:
        return (
            cls(
                config=data.get("config", None),
                state=data.get("state", None),
                description=data.get("description", ""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class UninitedAccountState(TlObject, AccountState):
    """Type for ``uninited.accountState``"""

    def __init__(self, frozen_hash: bytes = b"", extra_id: str = None) -> None:
        self.frozen_hash: bytes = b64decode(frozen_hash)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["uninited.accountState"]:
        return "uninited.accountState"

    def getClass(self) -> Literal["AccountState"]:
        return "AccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "frozen_hash": self.frozen_hash,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["UninitedAccountState", None]:
        return (
            cls(frozen_hash=data.get("frozen_hash", b""), extra_id=data.get("@extra"))
            if data
            else None
        )


class FullAccountState(TlObject, FullAccountState):
    """Type for ``fullAccountState``"""

    def __init__(
        self,
        address: AccountAddress = None,
        balance: int = 0,
        last_transaction_id: InternalTransactionId = None,
        block_id: TonBlockIdExt = None,
        sync_utime: int = 0,
        account_state: AccountState = None,
        revision: int = 0,
        extra_id: str = None,
    ) -> None:
        self.address: Union[AccountAddress, None] = address
        self.balance: int = int(balance)
        self.last_transaction_id: Union[
            InternalTransactionId, None
        ] = last_transaction_id
        self.block_id: Union[TonBlockIdExt, None] = block_id
        self.sync_utime: int = int(sync_utime)
        self.account_state: Union[
            RawAccountState,
            WalletV3AccountState,
            WalletV4AccountState,
            WalletHighloadV1AccountState,
            WalletHighloadV2AccountState,
            DnsAccountState,
            RwalletAccountState,
            PchanAccountState,
            UninitedAccountState,
            None,
        ] = account_state
        self.revision: int = int(revision)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["fullAccountState"]:
        return "fullAccountState"

    def getClass(self) -> Literal["FullAccountState"]:
        return "FullAccountState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "address": self.address,
            "balance": self.balance,
            "last_transaction_id": self.last_transaction_id,
            "block_id": self.block_id,
            "sync_utime": self.sync_utime,
            "account_state": self.account_state,
            "revision": self.revision,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["FullAccountState", None]:
        return (
            cls(
                address=data.get("address", None),
                balance=data.get("balance", 0),
                last_transaction_id=data.get("last_transaction_id", None),
                block_id=data.get("block_id", None),
                sync_utime=data.get("sync_utime", 0),
                account_state=data.get("account_state", None),
                revision=data.get("revision", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class AccountRevisionList(TlObject, AccountRevisionList):
    """Type for ``accountRevisionList``"""

    def __init__(
        self, revisions: List[FullAccountState] = None, extra_id: str = None
    ) -> None:
        self.revisions: List[FullAccountState] = revisions or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["accountRevisionList"]:
        return "accountRevisionList"

    def getClass(self) -> Literal["AccountRevisionList"]:
        return "AccountRevisionList"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "revisions": self.revisions,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["AccountRevisionList", None]:
        return (
            cls(revisions=data.get("revisions", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class AccountList(TlObject, AccountList):
    """Type for ``accountList``"""

    def __init__(
        self, accounts: List[FullAccountState] = None, extra_id: str = None
    ) -> None:
        self.accounts: List[FullAccountState] = accounts or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["accountList"]:
        return "accountList"

    def getClass(self) -> Literal["AccountList"]:
        return "AccountList"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "accounts": self.accounts,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["AccountList", None]:
        return (
            cls(accounts=data.get("accounts", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class SyncStateDone(TlObject, SyncState):
    """Type for ``syncStateDone``"""

    def __init__(self, extra_id: str = None) -> None:
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["syncStateDone"]:
        return "syncStateDone"

    def getClass(self) -> Literal["SyncState"]:
        return "SyncState"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["SyncStateDone", None]:
        return cls(extra_id=data.get("@extra")) if data else None


class SyncStateInProgress(TlObject, SyncState):
    """Type for ``syncStateInProgress``"""

    def __init__(
        self,
        from_seqno: int = 0,
        to_seqno: int = 0,
        current_seqno: int = 0,
        extra_id: str = None,
    ) -> None:
        self.from_seqno: int = int(from_seqno)
        self.to_seqno: int = int(to_seqno)
        self.current_seqno: int = int(current_seqno)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["syncStateInProgress"]:
        return "syncStateInProgress"

    def getClass(self) -> Literal["SyncState"]:
        return "SyncState"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "from_seqno": self.from_seqno,
            "to_seqno": self.to_seqno,
            "current_seqno": self.current_seqno,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["SyncStateInProgress", None]:
        return (
            cls(
                from_seqno=data.get("from_seqno", 0),
                to_seqno=data.get("to_seqno", 0),
                current_seqno=data.get("current_seqno", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class MsgDataRaw(TlObject, MsgData):
    """Type for ``msg.dataRaw``"""

    def __init__(
        self, body: bytes = b"", init_state: bytes = b"", extra_id: str = None
    ) -> None:
        self.body: bytes = b64decode(body)
        self.init_state: bytes = b64decode(init_state)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["msg.dataRaw"]:
        return "msg.dataRaw"

    def getClass(self) -> Literal["msg.Data"]:
        return "msg.Data"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "body": self.body,
            "init_state": self.init_state,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["MsgDataRaw", None]:
        return (
            cls(
                body=data.get("body", b""),
                init_state=data.get("init_state", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class MsgDataText(TlObject, MsgData):
    """Type for ``msg.dataText``"""

    def __init__(self, text: bytes = b"", extra_id: str = None) -> None:
        self.text: bytes = b64decode(text)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["msg.dataText"]:
        return "msg.dataText"

    def getClass(self) -> Literal["msg.Data"]:
        return "msg.Data"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "text": self.text, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["MsgDataText", None]:
        return (
            cls(text=data.get("text", b""), extra_id=data.get("@extra"))
            if data
            else None
        )


class MsgDataDecryptedText(TlObject, MsgData):
    """Type for ``msg.dataDecryptedText``"""

    def __init__(self, text: bytes = b"", extra_id: str = None) -> None:
        self.text: bytes = b64decode(text)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["msg.dataDecryptedText"]:
        return "msg.dataDecryptedText"

    def getClass(self) -> Literal["msg.Data"]:
        return "msg.Data"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "text": self.text, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["MsgDataDecryptedText", None]:
        return (
            cls(text=data.get("text", b""), extra_id=data.get("@extra"))
            if data
            else None
        )


class MsgDataEncryptedText(TlObject, MsgData):
    """Type for ``msg.dataEncryptedText``"""

    def __init__(self, text: bytes = b"", extra_id: str = None) -> None:
        self.text: bytes = b64decode(text)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["msg.dataEncryptedText"]:
        return "msg.dataEncryptedText"

    def getClass(self) -> Literal["msg.Data"]:
        return "msg.Data"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "text": self.text, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["MsgDataEncryptedText", None]:
        return (
            cls(text=data.get("text", b""), extra_id=data.get("@extra"))
            if data
            else None
        )


class MsgDataEncrypted(TlObject, MsgDataEncrypted):
    """Type for ``msg.dataEncrypted``"""

    def __init__(
        self, source: AccountAddress = None, data: MsgData = None, extra_id: str = None
    ) -> None:
        self.source: Union[AccountAddress, None] = source
        self.data: Union[
            MsgDataRaw, MsgDataText, MsgDataDecryptedText, MsgDataEncryptedText, None
        ] = data
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["msg.dataEncrypted"]:
        return "msg.dataEncrypted"

    def getClass(self) -> Literal["msg.DataEncrypted"]:
        return "msg.DataEncrypted"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "source": self.source,
            "data": self.data,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["MsgDataEncrypted", None]:
        return (
            cls(
                source=data.get("source", None),
                data=data.get("data", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class MsgDataDecrypted(TlObject, MsgDataDecrypted):
    """Type for ``msg.dataDecrypted``"""

    def __init__(
        self, proof: bytes = b"", data: MsgData = None, extra_id: str = None
    ) -> None:
        self.proof: bytes = b64decode(proof)
        self.data: Union[
            MsgDataRaw, MsgDataText, MsgDataDecryptedText, MsgDataEncryptedText, None
        ] = data
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["msg.dataDecrypted"]:
        return "msg.dataDecrypted"

    def getClass(self) -> Literal["msg.DataDecrypted"]:
        return "msg.DataDecrypted"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "proof": self.proof,
            "data": self.data,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["MsgDataDecrypted", None]:
        return (
            cls(
                proof=data.get("proof", b""),
                data=data.get("data", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class MsgDataEncryptedArray(TlObject, MsgDataEncryptedArray):
    """Type for ``msg.dataEncryptedArray``"""

    def __init__(
        self, elements: List[MsgDataEncrypted] = None, extra_id: str = None
    ) -> None:
        self.elements: List[MsgDataEncrypted] = elements or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["msg.dataEncryptedArray"]:
        return "msg.dataEncryptedArray"

    def getClass(self) -> Literal["msg.DataEncryptedArray"]:
        return "msg.DataEncryptedArray"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "elements": self.elements,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["MsgDataEncryptedArray", None]:
        return (
            cls(elements=data.get("elements", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class MsgDataDecryptedArray(TlObject, MsgDataDecryptedArray):
    """Type for ``msg.dataDecryptedArray``"""

    def __init__(
        self, elements: List[MsgDataDecrypted] = None, extra_id: str = None
    ) -> None:
        self.elements: List[MsgDataDecrypted] = elements or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["msg.dataDecryptedArray"]:
        return "msg.dataDecryptedArray"

    def getClass(self) -> Literal["msg.DataDecryptedArray"]:
        return "msg.DataDecryptedArray"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "elements": self.elements,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["MsgDataDecryptedArray", None]:
        return (
            cls(elements=data.get("elements", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class MsgMessage(TlObject, MsgMessage):
    """Type for ``msg.message``"""

    def __init__(
        self,
        destination: AccountAddress = None,
        public_key: str = "",
        amount: int = 0,
        data: MsgData = None,
        send_mode: int = 0,
        extra_id: str = None,
    ) -> None:
        self.destination: Union[AccountAddress, None] = destination
        self.public_key: Union[str, None] = public_key
        self.amount: int = int(amount)
        self.data: Union[
            MsgDataRaw, MsgDataText, MsgDataDecryptedText, MsgDataEncryptedText, None
        ] = data
        self.send_mode: int = int(send_mode)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["msg.message"]:
        return "msg.message"

    def getClass(self) -> Literal["msg.Message"]:
        return "msg.Message"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "destination": self.destination,
            "public_key": self.public_key,
            "amount": self.amount,
            "data": self.data,
            "send_mode": self.send_mode,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["MsgMessage", None]:
        return (
            cls(
                destination=data.get("destination", None),
                public_key=data.get("public_key", ""),
                amount=data.get("amount", 0),
                data=data.get("data", None),
                send_mode=data.get("send_mode", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class DnsEntryDataUnknown(TlObject, DnsEntryData):
    """Type for ``dns.entryDataUnknown``"""

    def __init__(self, bytes: bytes = b"", extra_id: str = None) -> None:
        self.bytes: bytes = b64decode(bytes)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.entryDataUnknown"]:
        return "dns.entryDataUnknown"

    def getClass(self) -> Literal["dns.EntryData"]:
        return "dns.EntryData"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "bytes": self.bytes, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsEntryDataUnknown", None]:
        return (
            cls(bytes=data.get("bytes", b""), extra_id=data.get("@extra"))
            if data
            else None
        )


class DnsEntryDataText(TlObject, DnsEntryData):
    """Type for ``dns.entryDataText``"""

    def __init__(self, text: str = "", extra_id: str = None) -> None:
        self.text: Union[str, None] = text
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.entryDataText"]:
        return "dns.entryDataText"

    def getClass(self) -> Literal["dns.EntryData"]:
        return "dns.EntryData"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "text": self.text, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsEntryDataText", None]:
        return (
            cls(text=data.get("text", ""), extra_id=data.get("@extra"))
            if data
            else None
        )


class DnsEntryDataNextResolver(TlObject, DnsEntryData):
    """Type for ``dns.entryDataNextResolver``"""

    def __init__(self, resolver: AccountAddress = None, extra_id: str = None) -> None:
        self.resolver: Union[AccountAddress, None] = resolver
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.entryDataNextResolver"]:
        return "dns.entryDataNextResolver"

    def getClass(self) -> Literal["dns.EntryData"]:
        return "dns.EntryData"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "resolver": self.resolver,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsEntryDataNextResolver", None]:
        return (
            cls(resolver=data.get("resolver", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class DnsEntryDataSmcAddress(TlObject, DnsEntryData):
    """Type for ``dns.entryDataSmcAddress``"""

    def __init__(
        self, smc_address: AccountAddress = None, extra_id: str = None
    ) -> None:
        self.smc_address: Union[AccountAddress, None] = smc_address
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.entryDataSmcAddress"]:
        return "dns.entryDataSmcAddress"

    def getClass(self) -> Literal["dns.EntryData"]:
        return "dns.EntryData"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "smc_address": self.smc_address,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsEntryDataSmcAddress", None]:
        return (
            cls(smc_address=data.get("smc_address", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class DnsEntryDataAdnlAddress(TlObject, DnsEntryData):
    """Type for ``dns.entryDataAdnlAddress``"""

    def __init__(self, adnl_address: AdnlAddress = None, extra_id: str = None) -> None:
        self.adnl_address: Union[AdnlAddress, None] = adnl_address
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.entryDataAdnlAddress"]:
        return "dns.entryDataAdnlAddress"

    def getClass(self) -> Literal["dns.EntryData"]:
        return "dns.EntryData"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "adnl_address": self.adnl_address,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsEntryDataAdnlAddress", None]:
        return (
            cls(
                adnl_address=data.get("adnl_address", None), extra_id=data.get("@extra")
            )
            if data
            else None
        )


class DnsEntryDataStorageAddress(TlObject, DnsEntryData):
    """Type for ``dns.entryDataStorageAddress``"""

    def __init__(self, bag_id: int = 0, extra_id: str = None) -> None:
        self.bag_id: int = int(bag_id)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.entryDataStorageAddress"]:
        return "dns.entryDataStorageAddress"

    def getClass(self) -> Literal["dns.EntryData"]:
        return "dns.EntryData"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "bag_id": self.bag_id, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsEntryDataStorageAddress", None]:
        return (
            cls(bag_id=data.get("bag_id", 0), extra_id=data.get("@extra"))
            if data
            else None
        )


class DnsEntry(TlObject, DnsEntry):
    """Type for ``dns.entry``"""

    def __init__(
        self,
        name: str = "",
        category: int = 0,
        entry: DnsEntryData = None,
        extra_id: str = None,
    ) -> None:
        self.name: Union[str, None] = name
        self.category: int = int(category)
        self.entry: Union[
            DnsEntryDataUnknown,
            DnsEntryDataText,
            DnsEntryDataNextResolver,
            DnsEntryDataSmcAddress,
            DnsEntryDataAdnlAddress,
            DnsEntryDataStorageAddress,
            None,
        ] = entry
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.entry"]:
        return "dns.entry"

    def getClass(self) -> Literal["dns.Entry"]:
        return "dns.Entry"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "name": self.name,
            "category": self.category,
            "entry": self.entry,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsEntry", None]:
        return (
            cls(
                name=data.get("name", ""),
                category=data.get("category", 0),
                entry=data.get("entry", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class DnsActionDeleteAll(TlObject, DnsAction):
    """Type for ``dns.actionDeleteAll``"""

    def __init__(self, extra_id: str = None) -> None:
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.actionDeleteAll"]:
        return "dns.actionDeleteAll"

    def getClass(self) -> Literal["dns.Action"]:
        return "dns.Action"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsActionDeleteAll", None]:
        return cls(extra_id=data.get("@extra")) if data else None


class DnsActionDelete(TlObject, DnsAction):
    """Type for ``dns.actionDelete``"""

    def __init__(self, name: str = "", category: int = 0, extra_id: str = None) -> None:
        self.name: Union[str, None] = name
        self.category: int = int(category)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.actionDelete"]:
        return "dns.actionDelete"

    def getClass(self) -> Literal["dns.Action"]:
        return "dns.Action"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "name": self.name,
            "category": self.category,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsActionDelete", None]:
        return (
            cls(
                name=data.get("name", ""),
                category=data.get("category", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class DnsActionSet(TlObject, DnsAction):
    """Type for ``dns.actionSet``"""

    def __init__(self, entry: DnsEntry = None, extra_id: str = None) -> None:
        self.entry: Union[DnsEntry, None] = entry
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.actionSet"]:
        return "dns.actionSet"

    def getClass(self) -> Literal["dns.Action"]:
        return "dns.Action"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "entry": self.entry, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsActionSet", None]:
        return (
            cls(entry=data.get("entry", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class DnsResolved(TlObject, DnsResolved):
    """Type for ``dns.resolved``"""

    def __init__(self, entries: List[DnsEntry] = None, extra_id: str = None) -> None:
        self.entries: List[DnsEntry] = entries or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["dns.resolved"]:
        return "dns.resolved"

    def getClass(self) -> Literal["dns.Resolved"]:
        return "dns.Resolved"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "entries": self.entries,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["DnsResolved", None]:
        return (
            cls(entries=data.get("entries", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class PchanPromise(TlObject, PchanPromise):
    """Type for ``pchan.promise``"""

    def __init__(
        self,
        signature: bytes = b"",
        promise_A: int = 0,
        promise_B: int = 0,
        channel_id: int = 0,
        extra_id: str = None,
    ) -> None:
        self.signature: bytes = b64decode(signature)
        self.promise_A: int = int(promise_A)
        self.promise_B: int = int(promise_B)
        self.channel_id: int = int(channel_id)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["pchan.promise"]:
        return "pchan.promise"

    def getClass(self) -> Literal["pchan.Promise"]:
        return "pchan.Promise"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "signature": self.signature,
            "promise_A": self.promise_A,
            "promise_B": self.promise_B,
            "channel_id": self.channel_id,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["PchanPromise", None]:
        return (
            cls(
                signature=data.get("signature", b""),
                promise_A=data.get("promise_A", 0),
                promise_B=data.get("promise_B", 0),
                channel_id=data.get("channel_id", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class PchanActionInit(TlObject, PchanAction):
    """Type for ``pchan.actionInit``"""

    def __init__(
        self,
        inc_A: int = 0,
        inc_B: int = 0,
        min_A: int = 0,
        min_B: int = 0,
        extra_id: str = None,
    ) -> None:
        self.inc_A: int = int(inc_A)
        self.inc_B: int = int(inc_B)
        self.min_A: int = int(min_A)
        self.min_B: int = int(min_B)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["pchan.actionInit"]:
        return "pchan.actionInit"

    def getClass(self) -> Literal["pchan.Action"]:
        return "pchan.Action"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "inc_A": self.inc_A,
            "inc_B": self.inc_B,
            "min_A": self.min_A,
            "min_B": self.min_B,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["PchanActionInit", None]:
        return (
            cls(
                inc_A=data.get("inc_A", 0),
                inc_B=data.get("inc_B", 0),
                min_A=data.get("min_A", 0),
                min_B=data.get("min_B", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class PchanActionClose(TlObject, PchanAction):
    """Type for ``pchan.actionClose``"""

    def __init__(
        self,
        extra_A: int = 0,
        extra_B: int = 0,
        promise: PchanPromise = None,
        extra_id: str = None,
    ) -> None:
        self.extra_A: int = int(extra_A)
        self.extra_B: int = int(extra_B)
        self.promise: Union[PchanPromise, None] = promise
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["pchan.actionClose"]:
        return "pchan.actionClose"

    def getClass(self) -> Literal["pchan.Action"]:
        return "pchan.Action"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "extra_A": self.extra_A,
            "extra_B": self.extra_B,
            "promise": self.promise,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["PchanActionClose", None]:
        return (
            cls(
                extra_A=data.get("extra_A", 0),
                extra_B=data.get("extra_B", 0),
                promise=data.get("promise", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class PchanActionTimeout(TlObject, PchanAction):
    """Type for ``pchan.actionTimeout``"""

    def __init__(self, extra_id: str = None) -> None:
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["pchan.actionTimeout"]:
        return "pchan.actionTimeout"

    def getClass(self) -> Literal["pchan.Action"]:
        return "pchan.Action"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["PchanActionTimeout", None]:
        return cls(extra_id=data.get("@extra")) if data else None


class RwalletActionInit(TlObject, RwalletAction):
    """Type for ``rwallet.actionInit``"""

    def __init__(self, config: RwalletConfig = None, extra_id: str = None) -> None:
        self.config: Union[RwalletConfig, None] = config
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["rwallet.actionInit"]:
        return "rwallet.actionInit"

    def getClass(self) -> Literal["rwallet.Action"]:
        return "rwallet.Action"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "config": self.config, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["RwalletActionInit", None]:
        return (
            cls(config=data.get("config", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class ActionNoop(TlObject, Action):
    """Type for ``actionNoop``"""

    def __init__(self, extra_id: str = None) -> None:
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["actionNoop"]:
        return "actionNoop"

    def getClass(self) -> Literal["Action"]:
        return "Action"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["ActionNoop", None]:
        return cls(extra_id=data.get("@extra")) if data else None


class ActionMsg(TlObject, Action):
    """Type for ``actionMsg``"""

    def __init__(
        self,
        messages: List[MsgMessage] = None,
        allow_send_to_uninited: bool = False,
        extra_id: str = None,
    ) -> None:
        self.messages: List[MsgMessage] = messages or []
        self.allow_send_to_uninited: bool = bool(allow_send_to_uninited)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["actionMsg"]:
        return "actionMsg"

    def getClass(self) -> Literal["Action"]:
        return "Action"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "messages": self.messages,
            "allow_send_to_uninited": self.allow_send_to_uninited,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["ActionMsg", None]:
        return (
            cls(
                messages=data.get("messages", None),
                allow_send_to_uninited=data.get("allow_send_to_uninited", False),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class ActionDns(TlObject, Action):
    """Type for ``actionDns``"""

    def __init__(self, actions: List[DnsAction] = None, extra_id: str = None) -> None:
        self.actions: List[DnsAction] = actions or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["actionDns"]:
        return "actionDns"

    def getClass(self) -> Literal["Action"]:
        return "Action"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "actions": self.actions,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["ActionDns", None]:
        return (
            cls(actions=data.get("actions", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class ActionPchan(TlObject, Action):
    """Type for ``actionPchan``"""

    def __init__(self, action: PchanAction = None, extra_id: str = None) -> None:
        self.action: Union[
            PchanActionInit, PchanActionClose, PchanActionTimeout, None
        ] = action
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["actionPchan"]:
        return "actionPchan"

    def getClass(self) -> Literal["Action"]:
        return "Action"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "action": self.action, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["ActionPchan", None]:
        return (
            cls(action=data.get("action", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class ActionRwallet(TlObject, Action):
    """Type for ``actionRwallet``"""

    def __init__(self, action: RwalletActionInit = None, extra_id: str = None) -> None:
        self.action: Union[RwalletActionInit, None] = action
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["actionRwallet"]:
        return "actionRwallet"

    def getClass(self) -> Literal["Action"]:
        return "Action"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "action": self.action, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["ActionRwallet", None]:
        return (
            cls(action=data.get("action", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class Fees(TlObject, Fees):
    """Type for ``fees``"""

    def __init__(
        self,
        in_fwd_fee: int = 0,
        storage_fee: int = 0,
        gas_fee: int = 0,
        fwd_fee: int = 0,
        extra_id: str = None,
    ) -> None:
        self.in_fwd_fee: int = int(in_fwd_fee)
        self.storage_fee: int = int(storage_fee)
        self.gas_fee: int = int(gas_fee)
        self.fwd_fee: int = int(fwd_fee)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["fees"]:
        return "fees"

    def getClass(self) -> Literal["Fees"]:
        return "Fees"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "in_fwd_fee": self.in_fwd_fee,
            "storage_fee": self.storage_fee,
            "gas_fee": self.gas_fee,
            "fwd_fee": self.fwd_fee,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["Fees", None]:
        return (
            cls(
                in_fwd_fee=data.get("in_fwd_fee", 0),
                storage_fee=data.get("storage_fee", 0),
                gas_fee=data.get("gas_fee", 0),
                fwd_fee=data.get("fwd_fee", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class QueryFees(TlObject, QueryFees):
    """Type for ``query.fees``"""

    def __init__(
        self,
        source_fees: Fees = None,
        destination_fees: List[Fees] = None,
        extra_id: str = None,
    ) -> None:
        self.source_fees: Union[Fees, None] = source_fees
        self.destination_fees: List[Fees] = destination_fees or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["query.fees"]:
        return "query.fees"

    def getClass(self) -> Literal["query.Fees"]:
        return "query.Fees"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "source_fees": self.source_fees,
            "destination_fees": self.destination_fees,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["QueryFees", None]:
        return (
            cls(
                source_fees=data.get("source_fees", None),
                destination_fees=data.get("destination_fees", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class QueryInfo(TlObject, QueryInfo):
    """Type for ``query.info``"""

    def __init__(
        self,
        id: int = 0,
        valid_until: int = 0,
        body_hash: bytes = b"",
        body: bytes = b"",
        init_state: bytes = b"",
        extra_id: str = None,
    ) -> None:
        self.id: int = int(id)
        self.valid_until: int = int(valid_until)
        self.body_hash: bytes = b64decode(body_hash)
        self.body: bytes = b64decode(body)
        self.init_state: bytes = b64decode(init_state)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["query.info"]:
        return "query.info"

    def getClass(self) -> Literal["query.Info"]:
        return "query.Info"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "id": self.id,
            "valid_until": self.valid_until,
            "body_hash": self.body_hash,
            "body": self.body,
            "init_state": self.init_state,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["QueryInfo", None]:
        return (
            cls(
                id=data.get("id", 0),
                valid_until=data.get("valid_until", 0),
                body_hash=data.get("body_hash", b""),
                body=data.get("body", b""),
                init_state=data.get("init_state", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class TvmSlice(TlObject, TvmSlice):
    """Type for ``tvm.slice``"""

    def __init__(self, bytes: bytes = b"", extra_id: str = None) -> None:
        self.bytes: bytes = b64decode(bytes)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["tvm.slice"]:
        return "tvm.slice"

    def getClass(self) -> Literal["tvm.Slice"]:
        return "tvm.Slice"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "bytes": self.bytes, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TvmSlice", None]:
        return (
            cls(bytes=data.get("bytes", b""), extra_id=data.get("@extra"))
            if data
            else None
        )


class TvmCell(TlObject, TvmCell):
    """Type for ``tvm.cell``"""

    def __init__(self, bytes: bytes = b"", extra_id: str = None) -> None:
        self.bytes: bytes = b64decode(bytes)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["tvm.cell"]:
        return "tvm.cell"

    def getClass(self) -> Literal["tvm.Cell"]:
        return "tvm.Cell"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "bytes": self.bytes, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TvmCell", None]:
        return (
            cls(bytes=data.get("bytes", b""), extra_id=data.get("@extra"))
            if data
            else None
        )


class TvmNumberDecimal(TlObject, TvmNumber):
    """Type for ``tvm.numberDecimal``"""

    def __init__(self, number: str = "", extra_id: str = None) -> None:
        self.number: Union[str, None] = number
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["tvm.numberDecimal"]:
        return "tvm.numberDecimal"

    def getClass(self) -> Literal["tvm.Number"]:
        return "tvm.Number"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "number": self.number, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TvmNumberDecimal", None]:
        return (
            cls(number=data.get("number", ""), extra_id=data.get("@extra"))
            if data
            else None
        )


class TvmTuple(TlObject, TvmTuple):
    """Type for ``tvm.tuple``"""

    def __init__(
        self, elements: List[TvmStackEntry] = None, extra_id: str = None
    ) -> None:
        self.elements: List[TvmStackEntry] = elements or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["tvm.tuple"]:
        return "tvm.tuple"

    def getClass(self) -> Literal["tvm.Tuple"]:
        return "tvm.Tuple"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "elements": self.elements,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TvmTuple", None]:
        return (
            cls(elements=data.get("elements", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class TvmList(TlObject, TvmList):
    """Type for ``tvm.list``"""

    def __init__(
        self, elements: List[TvmStackEntry] = None, extra_id: str = None
    ) -> None:
        self.elements: List[TvmStackEntry] = elements or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["tvm.list"]:
        return "tvm.list"

    def getClass(self) -> Literal["tvm.List"]:
        return "tvm.List"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "elements": self.elements,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TvmList", None]:
        return (
            cls(elements=data.get("elements", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class TvmStackEntrySlice(TlObject, TvmStackEntry):
    """Type for ``tvm.stackEntrySlice``"""

    def __init__(self, slice: TvmSlice = None, extra_id: str = None) -> None:
        self.slice: Union[TvmSlice, None] = slice
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["tvm.stackEntrySlice"]:
        return "tvm.stackEntrySlice"

    def getClass(self) -> Literal["tvm.StackEntry"]:
        return "tvm.StackEntry"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "slice": self.slice, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TvmStackEntrySlice", None]:
        return (
            cls(slice=data.get("slice", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class TvmStackEntryCell(TlObject, TvmStackEntry):
    """Type for ``tvm.stackEntryCell``"""

    def __init__(self, cell: TvmCell = None, extra_id: str = None) -> None:
        self.cell: Union[TvmCell, None] = cell
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["tvm.stackEntryCell"]:
        return "tvm.stackEntryCell"

    def getClass(self) -> Literal["tvm.StackEntry"]:
        return "tvm.StackEntry"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "cell": self.cell, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TvmStackEntryCell", None]:
        return (
            cls(cell=data.get("cell", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class TvmStackEntryNumber(TlObject, TvmStackEntry):
    """Type for ``tvm.stackEntryNumber``"""

    def __init__(self, number: TvmNumber = None, extra_id: str = None) -> None:
        self.number: Union[TvmNumberDecimal, None] = number
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["tvm.stackEntryNumber"]:
        return "tvm.stackEntryNumber"

    def getClass(self) -> Literal["tvm.StackEntry"]:
        return "tvm.StackEntry"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "number": self.number, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TvmStackEntryNumber", None]:
        return (
            cls(number=data.get("number", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class TvmStackEntryTuple(TlObject, TvmStackEntry):
    """Type for ``tvm.stackEntryTuple``"""

    def __init__(self, tuple: TvmTuple = None, extra_id: str = None) -> None:
        self.tuple: Union[TvmTuple, None] = tuple
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["tvm.stackEntryTuple"]:
        return "tvm.stackEntryTuple"

    def getClass(self) -> Literal["tvm.StackEntry"]:
        return "tvm.StackEntry"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "tuple": self.tuple, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TvmStackEntryTuple", None]:
        return (
            cls(tuple=data.get("tuple", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class TvmStackEntryList(TlObject, TvmStackEntry):
    """Type for ``tvm.stackEntryList``"""

    def __init__(self, list: TvmList = None, extra_id: str = None) -> None:
        self.list: Union[TvmList, None] = list
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["tvm.stackEntryList"]:
        return "tvm.stackEntryList"

    def getClass(self) -> Literal["tvm.StackEntry"]:
        return "tvm.StackEntry"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "list": self.list, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TvmStackEntryList", None]:
        return (
            cls(list=data.get("list", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class TvmStackEntryUnsupported(TlObject, TvmStackEntry):
    """Type for ``tvm.stackEntryUnsupported``"""

    def __init__(self, extra_id: str = None) -> None:
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["tvm.stackEntryUnsupported"]:
        return "tvm.stackEntryUnsupported"

    def getClass(self) -> Literal["tvm.StackEntry"]:
        return "tvm.StackEntry"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["TvmStackEntryUnsupported", None]:
        return cls(extra_id=data.get("@extra")) if data else None


class SmcInfo(TlObject, SmcInfo):
    """Type for ``smc.info``"""

    def __init__(self, id: int = 0, extra_id: str = None) -> None:
        self.id: int = int(id)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["smc.info"]:
        return "smc.info"

    def getClass(self) -> Literal["smc.Info"]:
        return "smc.Info"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "id": self.id, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["SmcInfo", None]:
        return cls(id=data.get("id", 0), extra_id=data.get("@extra")) if data else None


class SmcMethodIdNumber(TlObject, SmcMethodId):
    """Type for ``smc.methodIdNumber``"""

    def __init__(self, number: int = 0, extra_id: str = None) -> None:
        self.number: int = int(number)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["smc.methodIdNumber"]:
        return "smc.methodIdNumber"

    def getClass(self) -> Literal["smc.MethodId"]:
        return "smc.MethodId"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "number": self.number, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["SmcMethodIdNumber", None]:
        return (
            cls(number=data.get("number", 0), extra_id=data.get("@extra"))
            if data
            else None
        )


class SmcMethodIdName(TlObject, SmcMethodId):
    """Type for ``smc.methodIdName``"""

    def __init__(self, name: str = "", extra_id: str = None) -> None:
        self.name: Union[str, None] = name
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["smc.methodIdName"]:
        return "smc.methodIdName"

    def getClass(self) -> Literal["smc.MethodId"]:
        return "smc.MethodId"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "name": self.name, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["SmcMethodIdName", None]:
        return (
            cls(name=data.get("name", ""), extra_id=data.get("@extra"))
            if data
            else None
        )


class SmcRunResult(TlObject, SmcRunResult):
    """Type for ``smc.runResult``"""

    def __init__(
        self,
        gas_used: int = 0,
        stack: List[TvmStackEntry] = None,
        exit_code: int = 0,
        extra_id: str = None,
    ) -> None:
        self.gas_used: int = int(gas_used)
        self.stack: List[TvmStackEntry] = stack or []
        self.exit_code: int = int(exit_code)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["smc.runResult"]:
        return "smc.runResult"

    def getClass(self) -> Literal["smc.RunResult"]:
        return "smc.RunResult"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "gas_used": self.gas_used,
            "stack": self.stack,
            "exit_code": self.exit_code,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["SmcRunResult", None]:
        return (
            cls(
                gas_used=data.get("gas_used", 0),
                stack=data.get("stack", None),
                exit_code=data.get("exit_code", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class SmcLibraryEntry(TlObject, SmcLibraryEntry):
    """Type for ``smc.libraryEntry``"""

    def __init__(self, hash: int = 0, data: bytes = b"", extra_id: str = None) -> None:
        self.hash: int = int(hash)
        self.data: bytes = b64decode(data)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["smc.libraryEntry"]:
        return "smc.libraryEntry"

    def getClass(self) -> Literal["smc.LibraryEntry"]:
        return "smc.LibraryEntry"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "hash": self.hash,
            "data": self.data,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["SmcLibraryEntry", None]:
        return (
            cls(
                hash=data.get("hash", 0),
                data=data.get("data", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class SmcLibraryResult(TlObject, SmcLibraryResult):
    """Type for ``smc.libraryResult``"""

    def __init__(
        self, result: List[SmcLibraryEntry] = None, extra_id: str = None
    ) -> None:
        self.result: List[SmcLibraryEntry] = result or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["smc.libraryResult"]:
        return "smc.libraryResult"

    def getClass(self) -> Literal["smc.LibraryResult"]:
        return "smc.LibraryResult"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "result": self.result, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["SmcLibraryResult", None]:
        return (
            cls(result=data.get("result", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class SmcLibraryQueryExtOne(TlObject, SmcLibraryQueryExt):
    """Type for ``smc.libraryQueryExt.one``"""

    def __init__(self, hash: int = 0, extra_id: str = None) -> None:
        self.hash: int = int(hash)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["smc.libraryQueryExt.one"]:
        return "smc.libraryQueryExt.one"

    def getClass(self) -> Literal["smc.LibraryQueryExt"]:
        return "smc.LibraryQueryExt"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "hash": self.hash, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["SmcLibraryQueryExtOne", None]:
        return (
            cls(hash=data.get("hash", 0), extra_id=data.get("@extra")) if data else None
        )


class SmcLibraryQueryExtScanBoc(TlObject, SmcLibraryQueryExt):
    """Type for ``smc.libraryQueryExt.scanBoc``"""

    def __init__(
        self, boc: bytes = b"", max_libs: int = 0, extra_id: str = None
    ) -> None:
        self.boc: bytes = b64decode(boc)
        self.max_libs: int = int(max_libs)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["smc.libraryQueryExt.scanBoc"]:
        return "smc.libraryQueryExt.scanBoc"

    def getClass(self) -> Literal["smc.LibraryQueryExt"]:
        return "smc.LibraryQueryExt"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "boc": self.boc,
            "max_libs": self.max_libs,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["SmcLibraryQueryExtScanBoc", None]:
        return (
            cls(
                boc=data.get("boc", b""),
                max_libs=data.get("max_libs", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class SmcLibraryResultExt(TlObject, SmcLibraryResultExt):
    """Type for ``smc.libraryResultExt``"""

    def __init__(
        self,
        dict_boc: bytes = b"",
        libs_ok: List[int] = None,
        libs_not_found: List[int] = None,
        extra_id: str = None,
    ) -> None:
        self.dict_boc: bytes = b64decode(dict_boc)
        self.libs_ok: List[int] = libs_ok or []
        self.libs_not_found: List[int] = libs_not_found or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["smc.libraryResultExt"]:
        return "smc.libraryResultExt"

    def getClass(self) -> Literal["smc.LibraryResultExt"]:
        return "smc.LibraryResultExt"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "dict_boc": self.dict_boc,
            "libs_ok": self.libs_ok,
            "libs_not_found": self.libs_not_found,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["SmcLibraryResultExt", None]:
        return (
            cls(
                dict_boc=data.get("dict_boc", b""),
                libs_ok=data.get("libs_ok", None),
                libs_not_found=data.get("libs_not_found", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class UpdateSendLiteServerQuery(TlObject, Update):
    """Type for ``updateSendLiteServerQuery``"""

    def __init__(self, id: int = 0, data: bytes = b"", extra_id: str = None) -> None:
        self.id: int = int(id)
        self.data: bytes = b64decode(data)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["updateSendLiteServerQuery"]:
        return "updateSendLiteServerQuery"

    def getClass(self) -> Literal["Update"]:
        return "Update"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "id": self.id,
            "data": self.data,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["UpdateSendLiteServerQuery", None]:
        return (
            cls(
                id=data.get("id", 0),
                data=data.get("data", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class UpdateSyncState(TlObject, Update):
    """Type for ``updateSyncState``"""

    def __init__(self, sync_state: SyncState = None, extra_id: str = None) -> None:
        self.sync_state: Union[SyncStateDone, SyncStateInProgress, None] = sync_state
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["updateSyncState"]:
        return "updateSyncState"

    def getClass(self) -> Literal["Update"]:
        return "Update"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "sync_state": self.sync_state,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["UpdateSyncState", None]:
        return (
            cls(sync_state=data.get("sync_state", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class LogStreamDefault(TlObject, LogStream):
    """Type for ``logStreamDefault``"""

    def __init__(self, extra_id: str = None) -> None:
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["logStreamDefault"]:
        return "logStreamDefault"

    def getClass(self) -> Literal["LogStream"]:
        return "LogStream"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["LogStreamDefault", None]:
        return cls(extra_id=data.get("@extra")) if data else None


class LogStreamFile(TlObject, LogStream):
    """Type for ``logStreamFile``"""

    def __init__(
        self, path: str = "", max_file_size: int = 0, extra_id: str = None
    ) -> None:
        self.path: Union[str, None] = path
        self.max_file_size: int = int(max_file_size)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["logStreamFile"]:
        return "logStreamFile"

    def getClass(self) -> Literal["LogStream"]:
        return "LogStream"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "path": self.path,
            "max_file_size": self.max_file_size,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["LogStreamFile", None]:
        return (
            cls(
                path=data.get("path", ""),
                max_file_size=data.get("max_file_size", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class LogStreamEmpty(TlObject, LogStream):
    """Type for ``logStreamEmpty``"""

    def __init__(self, extra_id: str = None) -> None:
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["logStreamEmpty"]:
        return "logStreamEmpty"

    def getClass(self) -> Literal["LogStream"]:
        return "LogStream"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["LogStreamEmpty", None]:
        return cls(extra_id=data.get("@extra")) if data else None


class LogVerbosityLevel(TlObject, LogVerbosityLevel):
    """Type for ``logVerbosityLevel``"""

    def __init__(self, verbosity_level: int = 0, extra_id: str = None) -> None:
        self.verbosity_level: int = int(verbosity_level)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["logVerbosityLevel"]:
        return "logVerbosityLevel"

    def getClass(self) -> Literal["LogVerbosityLevel"]:
        return "LogVerbosityLevel"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "verbosity_level": self.verbosity_level,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["LogVerbosityLevel", None]:
        return (
            cls(
                verbosity_level=data.get("verbosity_level", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class LogTags(TlObject, LogTags):
    """Type for ``logTags``"""

    def __init__(self, tags: List[str] = None, extra_id: str = None) -> None:
        self.tags: List[str] = tags or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["logTags"]:
        return "logTags"

    def getClass(self) -> Literal["LogTags"]:
        return "LogTags"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "tags": self.tags, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["LogTags", None]:
        return (
            cls(tags=data.get("tags", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class Data(TlObject, Data):
    """Type for ``data``"""

    def __init__(self, bytes: bytes = b"", extra_id: str = None) -> None:
        self.bytes: bytes = b64decode(bytes)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["data"]:
        return "data"

    def getClass(self) -> Literal["Data"]:
        return "Data"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "bytes": self.bytes, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["Data", None]:
        return (
            cls(bytes=data.get("bytes", b""), extra_id=data.get("@extra"))
            if data
            else None
        )


class LiteServerInfo(TlObject, LiteServerInfo):
    """Type for ``liteServer.info``"""

    def __init__(
        self,
        now: int = 0,
        version: int = 0,
        capabilities: int = 0,
        extra_id: str = None,
    ) -> None:
        self.now: int = int(now)
        self.version: int = int(version)
        self.capabilities: int = int(capabilities)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["liteServer.info"]:
        return "liteServer.info"

    def getClass(self) -> Literal["liteServer.Info"]:
        return "liteServer.Info"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "now": self.now,
            "version": self.version,
            "capabilities": self.capabilities,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["LiteServerInfo", None]:
        return (
            cls(
                now=data.get("now", 0),
                version=data.get("version", 0),
                capabilities=data.get("capabilities", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class BlocksMasterchainInfo(TlObject, BlocksMasterchainInfo):
    """Type for ``blocks.masterchainInfo``"""

    def __init__(
        self,
        last: TonBlockIdExt = None,
        state_root_hash: bytes = b"",
        init: TonBlockIdExt = None,
        extra_id: str = None,
    ) -> None:
        self.last: Union[TonBlockIdExt, None] = last
        self.state_root_hash: bytes = b64decode(state_root_hash)
        self.init: Union[TonBlockIdExt, None] = init
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["blocks.masterchainInfo"]:
        return "blocks.masterchainInfo"

    def getClass(self) -> Literal["blocks.MasterchainInfo"]:
        return "blocks.MasterchainInfo"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "last": self.last,
            "state_root_hash": self.state_root_hash,
            "init": self.init,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["BlocksMasterchainInfo", None]:
        return (
            cls(
                last=data.get("last", None),
                state_root_hash=data.get("state_root_hash", b""),
                init=data.get("init", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class BlocksShards(TlObject, BlocksShards):
    """Type for ``blocks.shards``"""

    def __init__(
        self, shards: List[TonBlockIdExt] = None, extra_id: str = None
    ) -> None:
        self.shards: List[TonBlockIdExt] = shards or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["blocks.shards"]:
        return "blocks.shards"

    def getClass(self) -> Literal["blocks.Shards"]:
        return "blocks.Shards"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "shards": self.shards, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["BlocksShards", None]:
        return (
            cls(shards=data.get("shards", None), extra_id=data.get("@extra"))
            if data
            else None
        )


class BlocksAccountTransactionId(TlObject, BlocksAccountTransactionId):
    """Type for ``blocks.accountTransactionId``"""

    def __init__(self, account: bytes = b"", lt: int = 0, extra_id: str = None) -> None:
        self.account: bytes = b64decode(account)
        self.lt: int = int(lt)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["blocks.accountTransactionId"]:
        return "blocks.accountTransactionId"

    def getClass(self) -> Literal["blocks.AccountTransactionId"]:
        return "blocks.AccountTransactionId"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "account": self.account,
            "lt": self.lt,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["BlocksAccountTransactionId", None]:
        return (
            cls(
                account=data.get("account", b""),
                lt=data.get("lt", 0),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class BlocksShortTxId(TlObject, LiteServerTransactionId):
    """Type for ``blocks.shortTxId``"""

    def __init__(
        self,
        mode: int = 0,
        account: bytes = b"",
        lt: int = 0,
        hash: bytes = b"",
        extra_id: str = None,
    ) -> None:
        self.mode: int = int(mode)
        self.account: bytes = b64decode(account)
        self.lt: int = int(lt)
        self.hash: bytes = b64decode(hash)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["blocks.shortTxId"]:
        return "blocks.shortTxId"

    def getClass(self) -> Literal["liteServer.TransactionId"]:
        return "liteServer.TransactionId"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "mode": self.mode,
            "account": self.account,
            "lt": self.lt,
            "hash": self.hash,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["BlocksShortTxId", None]:
        return (
            cls(
                mode=data.get("mode", 0),
                account=data.get("account", b""),
                lt=data.get("lt", 0),
                hash=data.get("hash", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class BlocksTransactions(TlObject, BlocksTransactions):
    """Type for ``blocks.transactions``"""

    def __init__(
        self,
        id: TonBlockIdExt = None,
        req_count: int = 0,
        incomplete: bool = False,
        transactions: List[BlocksShortTxId] = None,
        extra_id: str = None,
    ) -> None:
        self.id: Union[TonBlockIdExt, None] = id
        self.req_count: int = int(req_count)
        self.incomplete: bool = bool(incomplete)
        self.transactions: List[BlocksShortTxId] = transactions or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["blocks.transactions"]:
        return "blocks.transactions"

    def getClass(self) -> Literal["blocks.Transactions"]:
        return "blocks.Transactions"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "id": self.id,
            "req_count": self.req_count,
            "incomplete": self.incomplete,
            "transactions": self.transactions,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["BlocksTransactions", None]:
        return (
            cls(
                id=data.get("id", None),
                req_count=data.get("req_count", 0),
                incomplete=data.get("incomplete", False),
                transactions=data.get("transactions", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class BlocksTransactionsExt(TlObject, BlocksTransactionsExt):
    """Type for ``blocks.transactionsExt``"""

    def __init__(
        self,
        id: TonBlockIdExt = None,
        req_count: int = 0,
        incomplete: bool = False,
        transactions: List[RawTransaction] = None,
        extra_id: str = None,
    ) -> None:
        self.id: Union[TonBlockIdExt, None] = id
        self.req_count: int = int(req_count)
        self.incomplete: bool = bool(incomplete)
        self.transactions: List[RawTransaction] = transactions or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["blocks.transactionsExt"]:
        return "blocks.transactionsExt"

    def getClass(self) -> Literal["blocks.TransactionsExt"]:
        return "blocks.TransactionsExt"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "id": self.id,
            "req_count": self.req_count,
            "incomplete": self.incomplete,
            "transactions": self.transactions,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["BlocksTransactionsExt", None]:
        return (
            cls(
                id=data.get("id", None),
                req_count=data.get("req_count", 0),
                incomplete=data.get("incomplete", False),
                transactions=data.get("transactions", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class BlocksHeader(TlObject, BlocksHeader):
    """Type for ``blocks.header``"""

    def __init__(
        self,
        id: TonBlockIdExt = None,
        global_id: int = 0,
        version: int = 0,
        flags: int = 0,
        after_merge: bool = False,
        after_split: bool = False,
        before_split: bool = False,
        want_merge: bool = False,
        want_split: bool = False,
        validator_list_hash_short: int = 0,
        catchain_seqno: int = 0,
        min_ref_mc_seqno: int = 0,
        is_key_block: bool = False,
        prev_key_block_seqno: int = 0,
        start_lt: int = 0,
        end_lt: int = 0,
        gen_utime: int = 0,
        vert_seqno: int = 0,
        prev_blocks: List[TonBlockIdExt] = None,
        extra_id: str = None,
    ) -> None:
        self.id: Union[TonBlockIdExt, None] = id
        self.global_id: int = int(global_id)
        self.version: int = int(version)
        self.flags: int = int(flags)
        self.after_merge: bool = bool(after_merge)
        self.after_split: bool = bool(after_split)
        self.before_split: bool = bool(before_split)
        self.want_merge: bool = bool(want_merge)
        self.want_split: bool = bool(want_split)
        self.validator_list_hash_short: int = int(validator_list_hash_short)
        self.catchain_seqno: int = int(catchain_seqno)
        self.min_ref_mc_seqno: int = int(min_ref_mc_seqno)
        self.is_key_block: bool = bool(is_key_block)
        self.prev_key_block_seqno: int = int(prev_key_block_seqno)
        self.start_lt: int = int(start_lt)
        self.end_lt: int = int(end_lt)
        self.gen_utime: int = int(gen_utime)
        self.vert_seqno: int = int(vert_seqno)
        self.prev_blocks: List[TonBlockIdExt] = prev_blocks or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["blocks.header"]:
        return "blocks.header"

    def getClass(self) -> Literal["blocks.Header"]:
        return "blocks.Header"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "id": self.id,
            "global_id": self.global_id,
            "version": self.version,
            "flags": self.flags,
            "after_merge": self.after_merge,
            "after_split": self.after_split,
            "before_split": self.before_split,
            "want_merge": self.want_merge,
            "want_split": self.want_split,
            "validator_list_hash_short": self.validator_list_hash_short,
            "catchain_seqno": self.catchain_seqno,
            "min_ref_mc_seqno": self.min_ref_mc_seqno,
            "is_key_block": self.is_key_block,
            "prev_key_block_seqno": self.prev_key_block_seqno,
            "start_lt": self.start_lt,
            "end_lt": self.end_lt,
            "gen_utime": self.gen_utime,
            "vert_seqno": self.vert_seqno,
            "prev_blocks": self.prev_blocks,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["BlocksHeader", None]:
        return (
            cls(
                id=data.get("id", None),
                global_id=data.get("global_id", 0),
                version=data.get("version", 0),
                flags=data.get("flags", 0),
                after_merge=data.get("after_merge", False),
                after_split=data.get("after_split", False),
                before_split=data.get("before_split", False),
                want_merge=data.get("want_merge", False),
                want_split=data.get("want_split", False),
                validator_list_hash_short=data.get("validator_list_hash_short", 0),
                catchain_seqno=data.get("catchain_seqno", 0),
                min_ref_mc_seqno=data.get("min_ref_mc_seqno", 0),
                is_key_block=data.get("is_key_block", False),
                prev_key_block_seqno=data.get("prev_key_block_seqno", 0),
                start_lt=data.get("start_lt", 0),
                end_lt=data.get("end_lt", 0),
                gen_utime=data.get("gen_utime", 0),
                vert_seqno=data.get("vert_seqno", 0),
                prev_blocks=data.get("prev_blocks", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class BlocksSignature(TlObject, BlocksSignature):
    """Type for ``blocks.signature``"""

    def __init__(
        self, node_id_short: int = 0, signature: bytes = b"", extra_id: str = None
    ) -> None:
        self.node_id_short: int = int(node_id_short)
        self.signature: bytes = b64decode(signature)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["blocks.signature"]:
        return "blocks.signature"

    def getClass(self) -> Literal["blocks.Signature"]:
        return "blocks.Signature"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "node_id_short": self.node_id_short,
            "signature": self.signature,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["BlocksSignature", None]:
        return (
            cls(
                node_id_short=data.get("node_id_short", 0),
                signature=data.get("signature", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class BlocksBlockSignatures(TlObject, BlocksBlockSignatures):
    """Type for ``blocks.blockSignatures``"""

    def __init__(
        self,
        id: TonBlockIdExt = None,
        signatures: List[BlocksSignature] = None,
        extra_id: str = None,
    ) -> None:
        self.id: Union[TonBlockIdExt, None] = id
        self.signatures: List[BlocksSignature] = signatures or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["blocks.blockSignatures"]:
        return "blocks.blockSignatures"

    def getClass(self) -> Literal["blocks.BlockSignatures"]:
        return "blocks.BlockSignatures"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "id": self.id,
            "signatures": self.signatures,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["BlocksBlockSignatures", None]:
        return (
            cls(
                id=data.get("id", None),
                signatures=data.get("signatures", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class BlocksShardBlockLink(TlObject, BlocksShardBlockLink):
    """Type for ``blocks.shardBlockLink``"""

    def __init__(
        self, id: TonBlockIdExt = None, proof: bytes = b"", extra_id: str = None
    ) -> None:
        self.id: Union[TonBlockIdExt, None] = id
        self.proof: bytes = b64decode(proof)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["blocks.shardBlockLink"]:
        return "blocks.shardBlockLink"

    def getClass(self) -> Literal["blocks.ShardBlockLink"]:
        return "blocks.ShardBlockLink"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "id": self.id,
            "proof": self.proof,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["BlocksShardBlockLink", None]:
        return (
            cls(
                id=data.get("id", None),
                proof=data.get("proof", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class BlocksBlockLinkBack(TlObject, BlocksBlockLinkBack):
    """Type for ``blocks.blockLinkBack``"""

    def __init__(
        self,
        to_key_block: bool = False,
        from_: TonBlockIdExt = None,
        to: TonBlockIdExt = None,
        dest_proof: bytes = b"",
        proof: bytes = b"",
        state_proof: bytes = b"",
        extra_id: str = None,
    ) -> None:
        self.to_key_block: bool = bool(to_key_block)
        self.from_: Union[TonBlockIdExt, None] = from_
        self.to: Union[TonBlockIdExt, None] = to
        self.dest_proof: bytes = b64decode(dest_proof)
        self.proof: bytes = b64decode(proof)
        self.state_proof: bytes = b64decode(state_proof)
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["blocks.blockLinkBack"]:
        return "blocks.blockLinkBack"

    def getClass(self) -> Literal["blocks.BlockLinkBack"]:
        return "blocks.BlockLinkBack"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "to_key_block": self.to_key_block,
            "from_": self.from_,
            "to": self.to,
            "dest_proof": self.dest_proof,
            "proof": self.proof,
            "state_proof": self.state_proof,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["BlocksBlockLinkBack", None]:
        return (
            cls(
                to_key_block=data.get("to_key_block", False),
                from_=data.get("from_", None),
                to=data.get("to", None),
                dest_proof=data.get("dest_proof", b""),
                proof=data.get("proof", b""),
                state_proof=data.get("state_proof", b""),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class BlocksShardBlockProof(TlObject, BlocksShardBlockProof):
    """Type for ``blocks.shardBlockProof``"""

    def __init__(
        self,
        from_: TonBlockIdExt = None,
        mc_id: TonBlockIdExt = None,
        links: List[BlocksShardBlockLink] = None,
        mc_proof: List[BlocksBlockLinkBack] = None,
        extra_id: str = None,
    ) -> None:
        self.from_: Union[TonBlockIdExt, None] = from_
        self.mc_id: Union[TonBlockIdExt, None] = mc_id
        self.links: List[BlocksShardBlockLink] = links or []
        self.mc_proof: List[BlocksBlockLinkBack] = mc_proof or []
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["blocks.shardBlockProof"]:
        return "blocks.shardBlockProof"

    def getClass(self) -> Literal["blocks.ShardBlockProof"]:
        return "blocks.ShardBlockProof"

    def to_dict(self) -> dict:
        data = {
            "@type": self.getType(),
            "from_": self.from_,
            "mc_id": self.mc_id,
            "links": self.links,
            "mc_proof": self.mc_proof,
            "@extra": self.extra_id,
        }

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["BlocksShardBlockProof", None]:
        return (
            cls(
                from_=data.get("from_", None),
                mc_id=data.get("mc_id", None),
                links=data.get("links", None),
                mc_proof=data.get("mc_proof", None),
                extra_id=data.get("@extra"),
            )
            if data
            else None
        )


class ConfigInfo(TlObject, ConfigInfo):
    """Type for ``configInfo``"""

    def __init__(self, config: TvmCell = None, extra_id: str = None) -> None:
        self.config: Union[TvmCell, None] = config
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["configInfo"]:
        return "configInfo"

    def getClass(self) -> Literal["ConfigInfo"]:
        return "ConfigInfo"

    def to_dict(self) -> dict:
        data = {"@type": self.getType(), "config": self.config, "@extra": self.extra_id}

        if not self.extra_id:
            del data["@extra"]

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["ConfigInfo", None]:
        return (
            cls(config=data.get("config", None), extra_id=data.get("@extra"))
            if data
            else None
        )
