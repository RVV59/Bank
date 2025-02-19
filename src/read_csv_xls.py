import os
import csv
import pandas as pd

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
path_csv = os.path.join(DATA_DIR, 'transactions.csv')
path_xls = os.path.join(DATA_DIR, 'transactions_excel.xlsx')


def read_csv_transactions(path_csv):
    """ Читает финансовые операции из CSV файла"""
    transactions = []

    with open(path_csv, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            transactions.append(row)
    return transactions


def read_excel_transactions(path_xlsx):
    """Читает финансовые операции из Excel файла"""
    df = pd.read_excel(path_xlsx)
    transactions = df.to_dict('records')
    return transactions
