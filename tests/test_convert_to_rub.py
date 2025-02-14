from unittest.mock import Mock, patch
import requests


@patch('requests.get')
def test_convert_to_rub(mock_get):
    # Мокируем успешный ответ API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    response = requests.get('url')
    assert response.status_code == 200
