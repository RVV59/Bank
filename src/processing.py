from typing import List, Dict


data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

def filter_by_state(list_payments, state='EXECUTED'):
    """принимает список словарей и опционально значение для ключа state  (по умолчанию
    'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state"""



    new_list = [pay for pay in data if pay.get('state') == state]
    return new_list


print(filter_by_state(data))

