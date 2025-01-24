import pytest

from src.generators import card_number_generator

start = 1
end = 15

@pytest.fixture
def card_numbers():
    return card_number_generator(start, end)

@pytest.mark.parametrize("start", [1, 15])
def test_card_number_generator(start, card_numbers):
    expected_results = card_numbers
    actual_results = list(card_numbers)
    assert actual_results == expected_results
