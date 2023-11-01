# TonX [![Version](https://img.shields.io/pypi/v/TonX?style=flat&logo=pypi)](https://pypi.org/project/TonX) [![Downloads](https://static.pepy.tech/personalized-badge/TonX?period=month&units=none&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/tonx)

TonX is an asynchronous [**Tonlib**](https://github.com/ton-blockchain/ton) wrapper for **TON** community written in **Python**.

### Features
- Easy, **Fast** and **Powerful**
- Fully **asynchronous**
- Supports **Payments**, **Wallet Tracker**, [**Tonlib**](https://github.com/ton-blockchain/ton) **types**/**functions** and much **more**.


### Requirements
> NOTE: [TonX](https://github.com/AYMENJD/tonx) will automatically attempt to download the correct pre-built binary of tonlibjson from  [**Tonlib Releases**](https://github.com/ton-blockchain/ton/releases)

- Python 3.9+

### Installation
You can install TonX using pip:

```bash
pip install tonx
```

To install with payments support, use:

```bash
pip install tonx[payments]
```

To install the development version from Github, use the following command:

```bash
pip install git+https://github.com/AYMENJD/tonx.git
```

## Examples

### Basic usage
Getting wallet **balance** of [**Fragment**](https://fragment.com):

```python
from tonx import Client, types, utils
from urllib.request import urlopen
import json, asyncio


async def main():
    ton_config = json.loads(
        urlopen("https://ton-blockchain.github.io/global.config.json").read()
    )  # Main net

    async with Client(
        config=ton_config,
        keystore=types.KeyStoreTypeDirectory("tonlib-db/"),
    ) as client:
        account_state = await client.getAccountState(
            types.AccountAddress("EQBAjaOyi2wGWlk-EDkSabqqnF-MrrwMadnwqrurKpkla9nE")
        )

        if account_state.getType() != "error":
            balance_in_toncoin = utils.from_nanograms(account_state.balance)

            print(
                f"Fragment.com wallet has {utils.truncate_zeros(balance_in_toncoin)} TON"
            )
        else:
            print(
                f"Something went wrong: {account_state.code} - {account_state.message}"
            )


asyncio.run(main())
```

### Payments
Accepting and handling **payments** in **TON**:

```python
from tonx import Client, types, utils
from tonx.payments import Payments, Invoice
from urllib.request import urlopen
import json, asyncio, logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s][p %(process)d %(threadName)s][%(created)f][%(filename)s:%(lineno)d][%(funcName)s]  %(message)s",
)


async def main():
    # ton_config = json.loads(
    #     urlopen("https://ton-blockchain.github.io/global.config.json").read()
    # ) # Main net
    ton_config = json.loads(
        urlopen("https://ton-blockchain.github.io/testnet-global.config.json").read()
    )  #  Test net

    client = Client(
        config=ton_config,
        keystore=types.KeyStoreTypeDirectory("tonlib-db/"),
    )
    payments = Payments(
        client=client,
        account_address=types.AccountAddress(
            "WALLET_ADDRESS"  # Wallet address that will receive the payments
        ),
    )

    @payments.on_invoicePayment()
    async def invoice_payment_handler(client, invoice: Invoice):
        if invoice.is_completed:
            payment_info = (
                f"Payment for Invoice #{invoice.id}\n"
                f"Amount: {utils.truncate_zeros(invoice.paid_amount)} TON\n"
                f"From: {utils.Address.normalize(invoice.paid_by_address)}\n"
                f"Is completed: {invoice.is_completed}\n"
                f"Extra: {invoice.extra}\n\n"
            )
        elif invoice.is_expired:
            payment_info = (
                f"Payment for expired Invoice #{invoice.id}\n"
                f"Amount: {utils.truncate_zeros(invoice.paid_amount)} TON\n"
                f"From: {utils.Address.normalize(invoice.paid_by_address)}\n"
                f"Is completed: {invoice.is_completed}\n"
                f"Extra: {invoice.extra}\n\n"
            )
        print(payment_info)

    await client.start(payments)

    # Create an example invoice
    invoice_1 = await payments.createInvoice(
        amount=0.05,
        comment="This is a test payment for TonX\n\n",
        extra={
            "name": "AYMEN",
            "user_id": 1088394097,
        },  # Extra data that will be stored with the invoice
        ttl=None,  # Invoice is valid for every with no expire time (NOTE: the default value for ttl is 3600 seconds a.k.a 1 hour)
    )

    invoice_2 = await payments.createInvoice(
        0.05,
        "This is a test payment for TonX\n\n",
        extra={"name": "AWM", "user_id": 39809485},
        ttl=300,  #  Invoice is valid for 5 minutes (the minimum value)
    )

    print(f"Payment link for invoice 1 ({invoice_1.id}): {invoice_1.payment_link}")
    print(f"Payment link for invoice 2 ({invoice_2.id}): {invoice_2.payment_link}")
    print()

    await client.idle(register_signal_handlers=True)


asyncio.run(main())
```

### Tracking
An example of **Tracking** a wallet **transactions**, for example [**@Wallet**](https://t.me/Wallet) Bot

```python
from tonx import Client, types, utils
from tonx.payments import Payments
from urllib.request import urlopen
import json, logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s][p %(process)d %(threadName)s][%(created)f][%(filename)s:%(lineno)d][%(funcName)s]  %(message)s",
)

ton_config = json.loads(
    urlopen("https://ton-blockchain.github.io/global.config.json").read()
)  # Main net

client = Client(
    config=ton_config,
    keystore=types.KeyStoreTypeDirectory("tonlib-db/"),
)
payments = Payments(
    client=client,
    account_address=types.AccountAddress(
        "EQBDanbCeUqI4_v-xrnAN0_I2wRvEIaLg1Qg2ZN5c6Zl1KOh"  # Wallet to watch transactions, for example t.me/Wallet address
    ),
)


@payments.on_incomingTransaction(
    filter_fn=lambda _, transaction: utils.from_nanograms(transaction.in_msg.value)
    >= 1  # Handle only transaction that is 1+ TON
)
async def handle_incoming_transactions(_, transaction: types.RawTransaction):
    comment = None
    if transaction.in_msg.msg_data.getType() == "msg.dataText":
        comment = transaction.in_msg.msg_data.text.decode()

    transaction_info = (
        f"Received a transaction:\n"
        f"Amount: `{utils.truncate_zeros(utils.from_nanograms(transaction.in_msg.value))} TON`\n"
        f"From: {utils.Address.normalize(transaction.in_msg.source)}\n"
        f"Comment: {comment}\n"
    )
    print(transaction_info)


@payments.on_outgoingTransaction()
async def handle_outgoing_transactions(_, transaction: types.RawTransaction):
    comment = None
    if transaction.out_msgs[0].msg_data.getType() == "msg.dataText":
        comment = transaction.out_msgs[0].msg_data.text.decode()

    transaction_info = (
        f"Sending "
        f"`{utils.truncate_zeros(utils.from_nanograms(transaction.out_msgs[0].value))} TON` "
        f"to `{utils.Address.normalize(transaction.out_msgs[0].destination)}` "
        f"({comment})\n"
    )
    print(transaction_info)


client.run(payments)
```
# License

MIT [License](https://github.com/AYMENJD/tonx/blob/main/LICENSE)
