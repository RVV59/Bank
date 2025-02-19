import pandas as pd
from unittest.mock import patch
from src.read_csv_xls import read_excel_transactions


def test_read_excel_transactions():
    # Создание фиктивного DataFrame
    index = [0, 1]
    columns = ['Date', 'Amount', 'Description']
    values = [['2020-01-01', '100', 'Income'], ['2020-02-15', '-50', 'Expense']]

    df_mock = pd.DataFrame(values, index=index, columns=columns)
    with patch.object(pd, 'read_excel', return_value=df_mock):
        result = read_excel_transactions("/path/to/file.xlsx")

    expected_result = [
        {'Date': '2020-01-01', 'Amount': '100', 'Description': 'Income'},
        {'Date': '2020-02-15', 'Amount': '-50', 'Description': 'Expense'}
    ]

    assert result == expected_result, f"Результат не совпадает! Получено: {result}, ожидаемое: {expected_result}"


test_read_excel_transactions()


def test_empty_excel_file():
    # Создание фиктивного DataFrame с пустыми данными
    df_mock = pd.DataFrame(columns=['Date', 'Amount', 'Description'])

    with patch.object(pd, 'read_excel', return_value=df_mock):
        result = read_excel_transactions("/path/to/empty_file.xlsx")

    expected_result = []

    assert result == expected_result, f"Результат не совпадает! Получено: {result}, ожидаемое: {expected_result}"
