import pytest

from src.generators import transaction_descriptions


@pytest.mark.parametrize(
    "data, expected", [([{"description": "Перевод организации", },
                         {"wrong_key": "Перевод со счета на счет", },
                         {"description": "Перевод с карты на карту", }, ],
                        ["Перевод организации", "", "Перевод с карты на карту"]),
                       ([], [])]
)
def test_transaction_descriptions(data, expected):
    assert list(transaction_descriptions(data)) == expected
