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
#
# #
# @pytest.mark.parametrize("input_card_number,expected_output", [
#     ("1234123412341234", "1234 12** **** 1234"),
#     ("9999888877776666", "9999 88** **** 6666"),
#     ("", ""),
#     ("1234567890", "1234567890")
# ])
# def test_get_mask_card_number(input_card_number, expected_output):
#     actual_output = get_mask_card_number(input_card_number)
#     assert actual_output == expected_output


# def test_get_mask_card_number(card_number: str) -> str:
#     if len(card_number) != 16:
#         raise ValueError("Длина номера карты должна быть 16 символов.")

#
# @pytest.mark.parametrize("input_account_number,expected_output", [
#     ("11111234567890123456", "**3456"),
#     ("11110987654321098765", "**8765")
# ])
# def test_get_mask_account(input_account_number, expected_output):
#     actual_output = get_mask_account(input_account_number)
#     assert actual_output == expected_output
#
#
# # def test_get_len_mask_card_account(card_number: str) -> str:
# #     if len(card_number) != 20:
# #         raise ValueError("Длина номера счета должна быть 20 символов.")
#
#
# @pytest.mark.parametrize("input_date,expected_output", [
#     ("2023-10-15", "15.10.2023"),
#     ("2000-01-01", "01.01.2000")
# ])
# def test_get_date(input_date, expected_output):
#     actual_output = get_date(input_date)
#     assert actual_output == expected_output
