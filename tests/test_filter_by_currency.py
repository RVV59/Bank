import pytest

from src.generators import filter_by_currency


@pytest.fixture
def usd_transactions():
    return list(filter_by_currency(transactions, "USD"))


@pytest.fixture
def eur_transactions():
    return list(filter_by_currency(transactions, "EUR"))


@pytest.mark.parametrize("states", [("EXECUTED", "FAILED")])
def test_filter_by_currency(states):
    if states == "EXECUTED":
        assert len(usd_transactions) == 2
        assert "USD" in usd_transactions[0]["operationAmount"]["currency"].values()
        assert "USD" in usd_transactions[1]["operationAmount"]["currency"].values()

    elif states == "FAILED":
        assert len(eur_transactions) == 1
        assert "EUR" in eur_transactions[0]["operationAmount"]["currency"].values()
