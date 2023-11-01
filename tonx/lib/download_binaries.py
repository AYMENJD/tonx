import os
import platform
import stat
import sys
import urllib.request

BINARIES = {
    "Darwin": {
        "x86_64": "https://github.com/ton-blockchain/ton/releases/latest/download/tonlibjson-mac-x86-64.dylib",
        "arm64": "https://github.com/ton-blockchain/ton/releases/latest/download/tonlibjson-mac-arm64.dylib",
    },
    "Windows": {
        "AMD64": "https://github.com/ton-blockchain/ton/releases/latest/download/tonlibjson.dll"
    },
    "Linux": {
        "x86_64": "https://github.com/ton-blockchain/ton/releases/latest/download/tonlibjson-linux-x86_64.so",
        "aarch64": "https://github.com/ton-blockchain/ton/releases/latest/download/tonlibjson-linux-arm64.so",
    },
}


def download_shared_library(url: str) -> None:
    filename = url.split("/")[-1]
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    urllib.request.urlretrieve(url, filepath)
    permissions = (
        stat.S_IRUSR
        | stat.S_IWUSR
        | stat.S_IRGRP
        | stat.S_IWGRP
        | stat.S_IROTH
        | stat.S_IWOTH
    )

    print(f"Shared library downloaded: {filepath}")
    try:
        os.chmod(filepath, permissions)
    except Exception as e:
        print(f"Couldn't change file permissions to {permissions}: {e}")


def get_binary_expected_path():
    system = platform.system()
    machine = platform.machine()

    if system in BINARIES and machine in BINARIES[system]:
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            BINARIES[system][machine].split("/")[-1],
        )


def binary_exists():
    if path := get_binary_expected_path():
        return os.path.exists(path)
    return False


def main():
    if __name__ == "__main__" and len(sys.argv) == 2 and sys.argv[1] == "all":
        for urls in BINARIES.values():
            for url in urls.values():
                download_shared_library(url)
    else:
        system = platform.system()
        machine = platform.machine()
        if system not in BINARIES or machine not in BINARIES[system]:
            raise Exception(
                f'No binary available for the system "{system}" and architecture "{machine}"'
            )
        else:
            download_shared_library(BINARIES[system][machine])


if __name__ == "__main__":
    print(f"System: {platform.system()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(
        f"Python Version: {platform.python_version()} ({', '.join(platform.python_build())})"
    )
    print(f"Python Implementation: {platform.python_implementation()}")
    print(f"Python Compiler: {platform.python_compiler()}")
    print(f"Release: {platform.release()}")
    print(f"OS: {platform.platform()}")
    print(f"OS Version: {platform.version()}\n")

    main()
