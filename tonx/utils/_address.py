import base64
import re
import tonx
from typing import Any, Dict, Union

BOUNCEABLE_TAG = 0x11
NON_BOUNCEABLE_TAG = 0x51
TEST_FLAG = 0x80

FRIENDLY_REGEX = re.compile(r"[A-Za-z0-9+/_-]+")
RAW_REGEX = re.compile(r"[a-f0-9]+")


# https://github.com/ton-org/ton-core/blob/main/src/utils/crc16.ts
def crc16(data):
    poly = 0x1021
    reg = 0
    message = bytearray(len(data) + 2)
    message[: len(data)] = data

    for byte in message:
        mask = 0x80
        while mask > 0:
            reg <<= 1
            if byte & mask:
                reg += 1
            mask >>= 1
            if reg > 0xFFFF:
                reg &= 0xFFFF
                reg ^= poly

    return bytes([(reg >> 8) & 0xFF, reg & 0xFF])


# https://github.com/ton-org/ton-core/blob/main/src/address/Address.ts
def parse_friendly_address(src: Union[str, bytes]) -> Dict[str, Any]:
    if isinstance(src, str) and not Address.is_friendly(src):
        raise ValueError("Unknown address type")

    data = src if isinstance(src, bytes) else base64.b64decode(src)

    if len(data) != 36:
        raise ValueError("Unknown address type: byte length is not equal to 36")

    addr = data[:34]
    crc = data[34:36]
    calced_crc = crc16(addr)
    if calced_crc != crc:
        raise ValueError("Invalid checksum: " + str(src))

    tag = addr[0]
    is_test_only = False
    is_bounceable = False

    if tag & TEST_FLAG:
        is_test_only = True
        tag = tag ^ TEST_FLAG

    if tag not in (BOUNCEABLE_TAG, NON_BOUNCEABLE_TAG):
        raise ValueError("Unknown address tag")

    is_bounceable = tag == BOUNCEABLE_TAG

    workchain = -1 if addr[1] == 0xFF else addr[1]
    hash_part = addr[2:]

    return {
        "is_test_only": is_test_only,
        "is_bounceable": is_bounceable,
        "workchain": workchain,
        "hash_part": hash_part,
    }


class Address:
    def __init__(
        self,
        workchain: int,
        hash_val: bytes,
    ):
        if len(hash_val) != 32:
            raise ValueError("Invalid address hash length: " + str(len(hash_val)))

        self.workchain = workchain
        self.hash = hash_val

    def to_raw_string(self) -> str:
        """Converts the address to a raw string representation

        Returns:
            :py:class:`str`:
                The raw string representation of the address
        """

        return f"{self.workchain}:{self.hash.hex()}"

    def to_raw(self) -> bytes:
        """Converts the address to a raw byte representation

        Returns:
            :py:class:`bytes`:
                The raw byte representation of the address
        """

        address_with_checksum = bytearray(36)
        address_with_checksum[:32] = self.hash
        address_with_checksum[32:] = bytes([self.workchain]) * 4
        return bytes(address_with_checksum)

    def to_string_buffer(
        self, test_only: bool = False, bounceable: bool = False
    ) -> bytes:
        """Converts the address to a byte buffer representation

        Args:
            test_only (``bool``, *optional*):
                Specifies if the address is for testing purposes only

            bounceable (``bool``, *optional*):
                Specifies if the address is bounceable

        Returns:
            :py:class:`bytes`:
                The byte buffer representation of the address
        """

        tag = BOUNCEABLE_TAG if bounceable else NON_BOUNCEABLE_TAG

        if test_only:
            tag |= TEST_FLAG

        addr = bytearray(34)
        addr[0] = tag
        addr[1] = 255 if self.workchain == -1 else self.workchain
        addr[2:] = self.hash
        address_with_checksum = bytearray(36)
        address_with_checksum[:34] = bytes(addr)
        address_with_checksum[34:] = crc16(bytes(addr))
        return bytes(address_with_checksum)

    def to_string(
        self,
        url_safe: bool = True,
        test_only: bool = False,
        bounceable: bool = False,
    ) -> str:
        """Converts the address to a string representation

        Args:
            url_safe (``bool``, *optional*):
                Specifies if the resulting string should be URL safe. Default is ``True``

            test_only (``bool``, *optional*):
                Specifies if the address is for testing purposes only. Default is ``False``

            bounceable (``bool``, *optional*):
                Specifies if the address is bounceable. Default is ``False``

        Returns:
            :py:class:`str`:
                The string representation of the address
        """
        buffer = self.to_string_buffer(test_only, bounceable)
        if url_safe:
            return base64.urlsafe_b64encode(buffer).decode().replace("=", "")
        else:
            return base64.b64encode(buffer).decode().replace("=", "")

    @staticmethod
    def is_friendly(source: str) -> bool:
        """Checks if the input address string is in friendly format

        Args:
            source (``str``):
                The address string to be checked

        Returns:
            :py:class:`bool`:
                ``True`` if the address is in a friendly format, ``False`` otherwise

        Example:
            .. code-block:: python

                is_friendly = Address.is_friendly("UQDQOvv1olHhrhVjRzHc8MJw5cUE2HkIzIOHPys8hRyajvnD")
                print(is_friendly)  # Output: True
        """

        if len(source) != 48:
            return False

        if not bool(FRIENDLY_REGEX.match(source)):
            return False

        return True

    @staticmethod
    def is_raw(source: str) -> bool:
        """Checks if the input address string is in raw format.

        Args:
            source (``str``):
                The address string to be checked.

        Returns:
            :py:class:`bool`:
                ``True`` if the address is in raw format, ``False`` otherwise.

        Example:
            .. code-block:: python

                is_raw = Address.is_raw("0:d03afbf5a251e1ae15634731dcf0c270e5c504d87908cc83873f2b3c851c9a8e")
                print(is_raw)  # Output: True
        """

        if ":" not in source:
            return False

        wc, hash_val = source.split(":")

        if not wc.isdigit():
            return False

        if not bool(RAW_REGEX.match(hash_val.lower())):
            return False

        if len(hash_val) != 64:
            return False

        return True

    @staticmethod
    def normalize(source: Union[str, "Address", "tonx.types.AccountAddress"]) -> str:
        """Normalizes the address representation to a standard string format

        Args:
            source (``str`` || :py:class:`~tonx.utils.Address`):
                The address string or :py:class:`~tonx.utils.Address` instance to be normalized

        Returns:
            :py:class:`str`:
                The normalized address string

        Example:
            .. code-block:: python

                normalized_address = Address.normalize("0:d03afbf5a251e1ae15634731dcf0c270e5c504d87908cc83873f2b3c851c9a8e")
                print(normalized_address)  # Output: 'UQDQOvv1olHhrhVjRzHc8MJw5cUE2HkIzIOHPys8hRyajvnD'
        """

        if isinstance(source, str):
            return Address.parse(source).to_string()
        elif isinstance(source, tonx.types.AccountAddress):
            return Address.parse(source.account_address).to_string()
        else:
            return source.to_string()

    @staticmethod
    def parse(source: str) -> "Address":
        """Parses the input address string and returns an :py:class:`~tonx.utils.Address` instance

        Args:
            source (``str``):
                The address string to be parsed.

        Returns:
            :py:class:`~tonx.utils.Address`:
                An :py:class:`~tonx.utils.Address` instance representing the parsed address

        Raises:
            :py:class:`ValueError`:
                If the address type is unknown or invalid
        """

        if Address.is_friendly(source):
            return Address.parse_friendly(source)
        elif Address.is_raw(source):
            return Address.parse_raw(source)
        else:
            raise ValueError("Unknown address type: " + source)

    @staticmethod
    def parse_raw(source: str) -> "Address":
        """Parses a raw address string and returns an :py:class:`~tonx.utils.Address` instance

        Args:
            source (``str``):
                The raw address string to be parsed

        Returns:
            :py:class:`~tonx.utils.Address`:
                An :py:class:`~tonx.utils.Address` instance representing the parsed raw address
        """

        workchain = int(source.split(":")[0])
        hash_val = bytes.fromhex(source.split(":")[1])
        return Address(workchain, hash_val)

    @staticmethod
    def parse_friendly(source: Union[str, bytes]) -> "Address":
        """Parses a friendly address string and returns an :py:class:`~tonx.utils.Address` instance

        Args:
            source (``str``):
                The friendly address string to be parsed

        Returns:
            :py:class:`~tonx.utils.Address`:
                An :py:class:`~tonx.utils.Address` instance representing the parsed friendly address
        """

        if isinstance(source, bytes):
            r = parse_friendly_address(source)
        else:
            addr = source.replace("-", "+").replace("_", "/")
            r = parse_friendly_address(addr)

        return Address(r["workchain"], r["hash_part"])

    def __str__(self) -> str:
        return self.to_string()
