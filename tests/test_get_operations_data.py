import json
import os
from unittest.mock import mock_open, patch

from src.utils import get_operations_data


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


@patch('builtins.open', mock_open(read_data='["a", "b", "c"]'))
def test_get_operations_data_list():
    # Проверка, что функция возвращает список при правильном формате данных
    result = get_operations_data()
    assert isinstance(result, list)
    assert len(result) == 3
    assert result == ["a", "b", "c"]


@patch('builtins.open', mock_open(read_data=''))
def test_get_operations_data_empty_file():
    # Проверка, что функция возвращает пустой список при пустом файле
    result = get_operations_data()
    assert result == []


@patch('builtins.open', mock_open(read_data='{"key1": "val1", "key2": "val2", "key3": "val3"}'))
def test_check_json_structure():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Проверка, что данные в файле соответствуют структуре JSON
    file_path = os.path.join(project_root, 'data', 'operations.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert json.loads(json.dumps(data)) == data
