from src.masks import get_date, get_mask_account, get_mask_card_number


def sort_transactions(transactions, reverse=False):
    """Сортирует транзакции по дате."""
    return sorted(transactions, key=lambda x: x.get('date', ''), reverse=reverse)


def filter_by_currency(transactions, currency='RUB'):
    """Фильтрует транзакции по валюте."""
    return [transaction for transaction in transactions if
            transaction.get('currency', 'RUB').upper() == currency.upper()]


def filter_by_description(transactions, keyword):
    """Фильтрует транзакции по ключевому слову в описании."""
    return [transaction for transaction in transactions if
            keyword.lower() in transaction.get('description', '').lower()]


def print_transactions(transactions):
    """Выводит транзакции в консоль."""
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return
    print(f"Всего банковских операций в выборке: {len(transactions)}\n")
    for transaction in transactions:
        print(f"{get_date(transaction['date'])} {transaction['description']}")
        if 'from' in transaction:
            print(f"{get_mask_card_number(transaction['from'])} -> {get_mask_account(transaction['to'])}")
        else:
            print(f"Счет **{transaction.get('to', 'XXXX')[-4:]}")
        print(f"Сумма: {transaction['operationAmount']['amount']} {transaction.get('currency', 'RUB')}\n")
