import os
import pytest
# import json
# import unittest
from unittest.mock import mock_open, patch
# Предполагаем, что функция get_operations_data() находится в файле operations.py
from src.utils import get_operations_data


# class TestGetOperationsData(unittest.TestCase):
#
#     @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1, "name": "Test Operation"}]')
#     def test_get_operations_data_success(self, mock_file):
#         # Вызов функции
#         result = get_operations_data()
#
#         # Проверка, что данные были загружены правильно
#         expected_data = [{"id": 1, "name": "Test Operation"}]
#         self.assertEqual(result, expected_data)
#
#         # Проверка, что open был вызван с правильным путем
#         project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         expected_file_path = os.path.join(project_root, 'data', 'operations.json')
#         mock_file.assert_called_once_with(expected_file_path, 'r', encoding='utf-8')
#
#     @patch('builtins.open', side_effect=FileNotFoundError)
#     def test_get_operations_data_file_not_found(self, mock_file):
#         # Проверка, что функция вызывает ошибку при отсутствии файла
#         with self.assertRaises(FileNotFoundError):
#             get_operations_data()
#
#
# if __name__ == '__main__':
#     unittest.main()


@patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1, "name": "Test Operation"}]')
def test_get_operations_data(mock_file):
    # Вызов функции
    result = get_operations_data()

    # Проверка, что данные были загружены правильно
    expected_data = [{"id": 1, "name": "Test Operation"}]
    assert result == expected_data

    # Проверка, что open был вызван с правильным путем
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    expected_file_path = os.path.join(project_root, 'data', 'operations.json')
    mock_file.assert_called_once_with(expected_file_path, 'r', encoding='utf-8')


@patch('builtins.open', side_effect=FileNotFoundError)
def test_get_operations_data(mock_file):

    # Проверка, что функция вызывает ошибку при отсутствии файла
    with pytest.raises(FileNotFoundError):
        get_operations_data()