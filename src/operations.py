import re
from collections import Counter
from src.utils import get_operations_data

transactions = get_operations_data()
search_pattern = r'EXECUTED'


def filter_transactions(transactions, search_pattern):
    """Фильтрует список транзакций по наличию строки, соответствующей регулярному выражению, в поле 'description'.
    """
    pattern = re.compile(search_pattern, re.IGNORECASE)

    filtered_transactions = []
    for transaction in transactions:
        description = transaction['state']
        # print(description)
        if pattern.search(description):
            filtered_transactions.append(transaction)
    return filtered_transactions


result = filter_transactions(transactions, search_pattern)
print(result)


categories = [transaction['description'] for transaction in transactions]


def count_transactions_by_category(transactions, categories):
    """
    Функция принимает список транзакций и список категорий, а возвращает словарь
    с количеством операций в каждой категории.
    """
    descriptions = [transaction.get('description', '').lower() for transaction in transactions]

    category_counter = Counter()
    for category in categories:
        category_lower = category.lower()
        count = sum(1 for description in descriptions if category_lower in description)
        category_counter[category] = count

    return dict(category_counter)
