import pytest


from src.widget import get_mask_account_card

@pytest.fixture
def valid_card_numbers():
    return ["111122223333444", "222233344455"]


def test_get_mask_account_card(valid_card_numbers):
    for card_number in valid_card_numbers:
        result = get_mask_account_card(card_number)
        assert len(result) == 19, "Длина результата должна быть 19"
        assert len(result) == 6, "Длина результата должна быть 6"