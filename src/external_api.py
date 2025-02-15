import os

import requests
from dotenv import load_dotenv

from src.utils import get_operations_data

load_dotenv()
EXCHANGE_RATES_API_KEY = os.getenv('EXCHANGE_RATES_API_KEY')

BASE_URL = 'https://api.apilayer.com/exchangerates_data/convert?to={RUB}&from={USD}&amount={amount}'

transactions = get_operations_data()


def convert_to_rub(transaction):
    '''принимает на вход транзакцию и возвращает сумму транзакции
     (amount) в рублях. Если транзакция была в USD или EUR, происходит
      обращение к внешнему API для получения текущего курса валют и
      конвертации суммы операции в рубли'''
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return float(amount)

    url = BASE_URL.format(RUB='RUB', USD=currency, amount=amount)
    headers = {
        'apikey': '0RgLK0gvykiHNF0JQAOHoL0SKmPYs6uP'
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            result = response.json()
            return round(float(result['result']), 2)
        else:
            raise Exception(f'Failed to get exchange rates: {response.text}')

    except Exception as e:
        print(f'An error occurred: {e}')
        return None


for transaction in transactions:
    print(convert_to_rub(transaction))
