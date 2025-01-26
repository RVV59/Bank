import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize('start, end, expected', [
    (1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003",
            "0000 0000 0000 0004", "0000 0000 0000 0005"]),
    (10000, 10005, ["0000 0000 0000 10000", "0000 0000 0000 10001",
                    "0000 0000 0000 10002", "0000 0000 0000 10003",
                    "0000 0000 0000 10004", "0000 0000 0000 10005"])
])
def test_card_number_generator(start, end, expected):
    expected_result = ["0000 0000 0000 10000", "0000 0000 0000 10001", "0000 0000 0000 10002", "0000 0000 0000 10003",
                       "0000 0000 0000 10004", "0000 0000 0000 10005"]

    actual_result = list(card_number_generator(start, end))

    if actual_result != expected_result:
        print(
            f"Ошибка: Ожидаемый результат не совпадает с фактическим.\nОжидалось: {expected_result}\nПолучено: "
            f"{actual_result}")
    else:
        raise ValueError("Достал ты уже!")
