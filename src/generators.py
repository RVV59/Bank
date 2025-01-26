transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 123456789,
        "state": "FAILED",
        "date": "2020-01-01T00:00:00.000000",
        "operationAmount": {
            "amount": "5000.00",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Карта 1111 2222 3333 4444",
        "to": "Карта 5555 6666 7777 8888"
    }
]


def filter_by_currency(transactions, cur_code):
    '''возвращаtnт итератор, выдающий транзакции с определенной валютой'''
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == cur_code:
            yield transaction


usd_transactions = filter_by_currency(transactions, "USD")
first_usd_transaction = next(usd_transactions)
for _ in range(2):
    print(first_usd_transaction)


def transaction_descriptions(transactions):
    '''возвращает описание каждой операции по очереди'''
    for transaction in transactions:
        yield (transaction.get("description", ""))


trnsctn_dscrptns = transaction_descriptions(transactions)
for _ in range(len(transactions)):
    print(next(trnsctn_dscrptns))


def card_number_generator(start, end):
    '''Генерация номеров банковских карт'''
    for number in range(start, end + 1):
        # formatted_number = format(number, '016')
        formatted_number = f"{number:016d}"
        spaced_number = ' '.join([formatted_number[i:i + 4] for i in range(0, len(formatted_number), 4)])
        yield spaced_number


for card_number in card_number_generator(1, 5):
    print(card_number)
