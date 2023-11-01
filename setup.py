from re import findall
from setuptools import setup, find_packages


with open("tonx/__init__.py", "r") as f:
    version = findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", "r") as f:
    readme = f.read()

# with open("requirements.txt", "r") as f:
#     requirements = [x.strip() for x in f.readlines()]

setup(
    name="TonX",
    version=version,
    description="A user-friendly Python library for interacting with TON (The Open Network), offering convenient payment handling and much more.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="AYMEN Mohammed",
    author_email="let.me.code.safe@gmail.com",
    url="https://github.com/AYMENJD/tonx",
    license="MIT",
    python_requires=">=3.9",
    extras_require={
        "payments": [
            "kvsqlite",
        ]
    },
    project_urls={
        "Source": "https://github.com/AYMENJD/tonx",
        "Tracker": "https://github.com/AYMENJD/tonx/issues",
    },
    packages=find_packages(exclude=["examples", "docs"]),
    package_data={
        "tonx": ["lib/*", "tonlib_api.*"],
    },
    keywords=[
        "ton",
        "telegram",
        "cryptocurrency",
        "blockchain",
        "tonlib",
        "payments",
        "crypto",
        "digital currency",
        "decentralized",
        "smart contracts",
        "dApp",
        "Ethereum",
        "Bitcoin",
        "cryptocurrency payments",
        "crypto wallet",
        "transaction",
        "secure",
        "privacy",
        "token",
        "block explorer",
        "smart contract development",
    ],
)
