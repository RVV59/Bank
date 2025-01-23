@pytest.fixture
def descriptions():
    return list(transaction_descriptions(transactions))# Параметризация для проверки различных типов описаний транзакций

@pytest.fixture
def descriptions():
    return list(transaction_descriptions(transactions))

@pytest.mark.parametrize("descriptions", [("Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту")])
def test_transaction_descriptions(descriptions):
    assert descriptions == descriptions