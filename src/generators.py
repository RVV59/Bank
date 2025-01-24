transactions =[
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


def filter_by_currency(transactions, cur_cod):
    '''возвращаtnт итератор, выдающий транзакции с определенной валютой'''
    for transaction in transactions:  # Проходимся по всем транзакциям
        if transaction["operationAmount"]["currency"]["code"] == cur_cod:  # Проверяем валюту транзакции
            yield transaction

usd_transactions = filter_by_currency(transactions, "EUR")
first_usd_transaction = next(usd_transactions)
# print(first_usd_transaction)
for _ in range(2):
    print(first_usd_transaction)
# Генерация описаний транзакций


def transaction_descriptions(transactions):
    for transaction in transactions:  # Проходимся по всем транзакциям
        yield transaction.get("description", "")  # Получаем описание транзакции или пустую строку, если нет описания


trnsctn_dscrptns = transaction_descriptions(transactions)
dscrptns_trnsctn = next(trnsctn_dscrptns)
print(dscrptns_trnsctn)


# Генерация номеров банковских карт
def card_number_generator(start=1, end=15):
    for number in range(start, end + 1):  # Проходимся по числам в заданном диапазоне
        formatted_number = format(number, '016')  # Преобразуем число в строку длиной 16 символов, дополняя нулями слева
        spaced_number = ' '.join([formatted_number[i:i+4] for i in range(0, len(formatted_number), 4)])  # Разделяем строку пробелами каждые 4 символа
        yield spaced_number  # Возвращаем номер банковской карты

# crd_nmbr_gnrtr = card_number_generator(start=1, end=10000)
# gnrt_nmbr_crd = next(crd_nmbr_gnrtr)
# print(gnrt_nmbr_crd)


for card_number in card_number_generator(1, 5):

    print(card_number)