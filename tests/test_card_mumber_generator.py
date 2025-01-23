 теста для функции card_number_generator:


import pytest

# Данные для тестирования
start = 1
end = 10000

# Фикстура для тестирования
@pytest.fixture
def card_numbers():
    return list(card_number_generator(start, end))

@pytest.mark.parametrize("start", [1, 10000])
def test_card_number_generator(start):
    actual_result = card_numbers[start:end]
    expected_result = ['0000' * 16 + ' ' * 4 for i in range(start, end + 1)]
    assert actual_result == expected_result