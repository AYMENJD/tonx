from ctypes.util import find_library
from ctypes import *
from logging import getLogger
import tonx

logger = getLogger(__name__)


class TonApi:
    def __init__(self, lib_path: str = None, verbosity: int = 2) -> None:
        if lib_path is None:
            lib_path = self.get_lib_path()

        if not lib_path:
            raise ValueError("tonapi library not found")

        logger.info(f"Initializing tonapi client with library: {lib_path}")
        self._build_client(lib_path, verbosity)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def get_lib_path(self) -> str:
        if lib_path := find_library("tonlibjson"):
            return lib_path

        expected_path = tonx.lib.get_binary_expected_path()
        if expected_path and tonx.lib.binary_exists():
            return expected_path

        tonx.lib.main()
        return expected_path or ""

    def _build_client(self, lib_path: str, verbosity: int) -> None:
        tonlib = CDLL(lib_path)

        tonlib_json_client_create = tonlib.tonlib_client_json_create
        tonlib_json_client_create.restype = c_void_p
        tonlib_json_client_create.argtypes = []

        self.__client = tonlib_json_client_create()

        tonlib_client_set_verbosity_level = tonlib.tonlib_client_set_verbosity_level
        tonlib_client_set_verbosity_level.restype = None
        tonlib_client_set_verbosity_level.argtypes = [c_int]
        self.set_verbosity_level = tonlib_client_set_verbosity_level

        self.set_verbosity_level(verbosity)

        tonlib_json_client_send = tonlib.tonlib_client_json_send
        tonlib_json_client_send.restype = None
        tonlib_json_client_send.argtypes = [c_void_p, c_char_p]
        self.__tonlib_send = tonlib_json_client_send

        tonlib_json_client_receive = tonlib.tonlib_client_json_receive
        tonlib_json_client_receive.restype = c_char_p
        tonlib_json_client_receive.argtypes = [c_void_p, c_double]
        self.__tonlib_receive = tonlib_json_client_receive

        tonlib_json_client_execute = tonlib.tonlib_client_json_execute
        tonlib_json_client_execute.restype = c_char_p
        tonlib_json_client_execute.argtypes = [c_void_p, c_char_p]
        self.__tonlib_execute = tonlib_json_client_execute

        tonlib_json_client_destroy = tonlib.tonlib_client_json_destroy
        tonlib_json_client_destroy.restype = None
        tonlib_json_client_destroy.argtypes = [c_void_p]
        self.__tonlib_destroy = tonlib_json_client_destroy

    def receive(self, timeout: float = 2.0) -> str:
        if res := self.__tonlib_receive(self.__client, c_double(timeout)):
            return res.decode("utf-8")

    def send(self, data: str) -> None:
        self.__tonlib_send(
            self.__client,
            data.encode("utf-8"),
        )

    def execute(self, data: str) -> str:
        if res := self.__tonlib_execute(self.__client, data.encode("utf-8")):
            return res.decode("utf-8")

    def destroy(self):
        self.__tonlib_destroy(self.client)
