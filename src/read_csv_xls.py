import os, csv, pandas as pd

from mypy.strconv import indent


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
path_csv = os.path.join(DATA_DIR, 'transactions.csv')
path_xls = os.path.join(DATA_DIR, 'transactions_excel.xlsx')
# Теперь вы можете передать эти переменные в ваши функции для чтения данных:


# path_csv = read_csv_transactions(CSV_FILE_PATH)
# path_excel = read_excel_transactions(EXCEL_FILE_PATH)
#
# def read_csv_transactions(path_csv):
#     """
#     Читает финансовые операции из CSV файла с разделителем ';'.
#
#     :param file_path: Путь до CSV файла.
#     :return: Список словарей с транзакциями.
#     """
#     transactions = []
#
#     with open(path_csv, 'r', encoding='utf-8') as file:
#         reader = csv.DictReader(file, delimiter=';')
#         for row in reader:
#             transactions.append(row)
#
#     return transactions


# print(read_csv_transactions(path_csv))

def read_excel_transactions(path_xlsx):
    """Читает финансовые операции из Excel файла"""
    df = pd.read_excel(path_xlsx)
    transactions = df.to_dict('records')
    return transactions


print(read_excel_transactions(path_xls))