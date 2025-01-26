import pytest

from src.generators import transaction_descriptions


# @pytest.fixture
# def descriptions():
#     return list(transaction_descriptions(transactions), "")
#
#
# @pytest.mark.parametrize("descriptions", [("Перевод организации", "Перевод со счета на счет",
#                                            "Перевод с карты на карту"
#                                            , "")])
# def test_transaction_descriptions(descriptions):
#     assert descriptions == descriptions


@pytest.mark.parametrize(
    "data, expected", [([{"description": "Перевод организации",},
                         {"wrong_key": "Перевод со счета на счет",},
                         {"description": "Перевод с карты на карту",},],
                         ["Перевод организации", "", "Перевод с карты на карту"]),
                       ([], [])]
)
def test_transaction_descriptions(data, expected):
    asseZrt list(transaction_descriptions(data)) == expected