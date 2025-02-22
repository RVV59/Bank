import pytest
from src.sort_filter_transactions import print_transactions, filter_by_description, filter_by_currency, sort_transactions

# Пример данных для тестирования
transactions = [
    {'date': '2023-10-01T12:34:56.789000', 'description': 'Покупка в магазине', 'currency': 'RUB', 'operationAmount': {'amount': 1000}, 'to': '1234567890'},
    {'date': '2023-09-15T12:34:56.789000', 'description': 'Оплата услуг', 'currency': 'USD', 'operationAmount': {'amount': 50}, 'to': '0987654321'},
    {'date': '2023-10-05T12:34:56.789000', 'description': 'Перевод другу', 'currency': 'RUB', 'operationAmount': {'amount': 500}, 'from': '1234123412341234', 'to': '5678567856785678'},
    {'date': '2023-08-20T12:34:56.789000', 'description': 'Покупка билетов', 'currency': 'EUR', 'operationAmount': {'amount': 200}, 'to': '1122334455'},
]

def test_sort_transactions():
    # Тест сортировки по возрастанию даты
    sorted_transactions = sort_transactions(transactions)
    assert sorted_transactions[0]['date'] == '2023-08-20T12:34:56.789000'
    assert sorted_transactions[-1]['date'] == '2023-10-05T12:34:56.789000'

    # Тест сортировки по убыванию даты
    sorted_reverse = sort_transactions(transactions, reverse=True)
    assert sorted_reverse[0]['date'] == '2023-10-05T12:34:56.789000'
    assert sorted_reverse[-1]['date'] == '2023-08-20T12:34:56.789000'

def test_filter_by_currency():
    # Тест фильтрации по валюте RUB
    rub_transactions = filter_by_currency(transactions, 'RUB')
    assert len(rub_transactions) == 2
    assert all(t['currency'] == 'RUB' for t in rub_transactions)

    # Тест фильтрации по валюте USD
    usd_transactions = filter_by_currency(transactions, 'USD')
    assert len(usd_transactions) == 1
    assert all(t['currency'] == 'USD' for t in usd_transactions)

    # Тест фильтрации по валюте EUR
    eur_transactions = filter_by_currency(transactions, 'EUR')
    assert len(eur_transactions) == 1
    assert all(t['currency'] == 'EUR' for t in eur_transactions)

def test_filter_by_description():
    # Тест фильтрации по ключевому слову "Покупка"
    keyword = 'Покупка'
    filtered_transactions = filter_by_description(transactions, keyword)
    assert len(filtered_transactions) == 2
    assert all(keyword.lower() in t['description'].lower() for t in filtered_transactions)

    # Тест фильтрации по ключевому слову "Перевод"
    keyword = 'Перевод'
    filtered_transactions = filter_by_description(transactions, keyword)
    assert len(filtered_transactions) == 1
    assert all(keyword.lower() in t['description'].lower() for t in filtered_transactions)

def test_print_transactions(capsys):
    # Тест на вывод пустого списка
    print_transactions([])
    captured = capsys.readouterr()
    assert "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации." in captured.out

    # Тест на вывод списка транзакций
    print_transactions(transactions)
    captured = capsys.readouterr()
    assert "Всего банковских операций в выборке: 4" in captured.out
    assert "Покупка в магазине" in captured.out
    assert "Оплата услуг" in captured.out
    assert "Перевод другу" in captured.out
    assert "Покупка билетов" in captured.out