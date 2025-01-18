import pytest

from src.masks import get_mask_card_number, get_mask_account, get_date


@pytest.mark.parametrize(
    "card_number, expected_exception",
    [
        ("1234123412341234", None),
        ("12341234", ValueError),
        ("", ValueError),
        ("123412341234123X", ValueError),
        ("ABCDEF1234567890", ValueError),
    ],
)
def test_get_mask_card_number(card_number, expected_exception):
    if expected_exception is None:
        get_mask_card_number(card_number)
    else:
        with pytest.raises(expected_exception):
            get_mask_card_number(card_number)

@pytest.mark.parametrize("card_mask,expected_output",
[
        ("12341234123412345555", None),
        ("12341234", ValueError),
        ("", ValueError),
        ("123412341234123X1111", ValueError),
        ("ABCDEF12345678901111", ValueError),
    ],
)
def test_get_mask_account(card_mask, expected_output):
    if expected_output is None:
        get_mask_account(card_mask)
    else:
        with pytest.raises(expected_output):
            get_mask_account(card_mask)


#     ("11111234567890123456", "**3456"),
#     ("11110987654321098765", "**8765")
# ])
# def test_get_mask_account(input_account_number, expected_output):
#     actual_output = get_mask_account(input_account_number)
#     assert actual_output == expected_output
#


@pytest.mark.parametrize("input_date,expected_output", [
    ("2023-10-15", "15.10.2023"),
    ("2000-01-01", "01.01.2000")
])
def test_get_date(input_date, expected_output):
    actual_output = get_date(input_date)
    assert actual_output == expected_output
