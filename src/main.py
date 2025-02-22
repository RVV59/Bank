from src.utils import get_operations_data
from src.operations import filter_transactions
from sort_filter_transactions import sort_transactions, filter_by_currency, filter_by_description, print_transactions


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ")
    if choice == '1':
        print("Для обработки выбран JSON-файл.")
    elif choice == '2':
        print("Для обработки выбран CSV-файл.")
    elif choice == '3':
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Завершение программы.")
        return

    transactions = get_operations_data()

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. Доступные статусы: EXECUTED, CANCELED, "
            "PENDING: ").upper()
        if status in ['EXECUTED', 'CANCELED', 'PENDING']:
            break
        print(f"Статус операции '{status}' недоступен.")

    filtered_transactions = filter_transactions(transactions, status)
    print(f"Операции отфильтрованы по статусу '{status}'.")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice == 'да':
        order_choice = input("Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию): ").lower()
        reverse = order_choice == 'по убыванию'
        filtered_transactions = sort_transactions(filtered_transactions, reverse)

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if currency_choice == 'да':
        filtered_transactions = filter_by_currency(filtered_transactions, 'RUB')

    keyword_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if keyword_choice == 'да':
        keyword = input("Введите ключевое слово для фильтрации: ")
        filtered_transactions = filter_by_description(filtered_transactions, keyword)

    print("Распечатываю итоговый список транзакций...")
    print_transactions(filtered_transactions)


if __name__ == "__main__":
    main()
