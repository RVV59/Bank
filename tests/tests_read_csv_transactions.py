import pytest
import unittest.mock as mock
from unittest.mock import patch
from src.read_csv_xls import read_csv_transactions


def test_read_csv_transactions():
    # Фиктивные данные для CSV
    data = """Date;Amount;Description
2020-01-01;100;Income
2020-02-15;-50;Expense"""

    # проверка метода open(), чтобы симулировать чтение из файла
    with patch("builtins.open", mock.mock_open(read_data=data)):
        result = read_csv_transactions("/path/to/file.csv")

    expected_result = [
        {'Date': '2020-01-01', 'Amount': '100', 'Description': 'Income'},
        {'Date': '2020-02-15', 'Amount': '-50', 'Description': 'Expense'}
    ]

    assert result == expected_result, f"Результат не совпадает! Получено: {result}, ожидаемое: {expected_result}"


def test_missing_csv_file():
    # тест метода open() для эмуляции отсутствия файла
    with patch("builtins.open") as mocked_open:
        mocked_open.side_effect = FileNotFoundError
        with pytest.raises(FileNotFoundError):
            read_csv_transactions("/path/to/missing_file.csv")
