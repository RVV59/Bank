# Программа "Bank"

## Основная цель программы "Банк"
### Банк работает со счетами клиентов, неустанно расширяя спектр услуг
### IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. 

## Реализовано функции:
1. Функцию маскировки номера банковской карты 
2. Функцию маскировки номера банковского счета
3. Сортировка по статусу сделок и дате их совершения

## Widget
* Этот модуль будет содержать функции для работы с новыми возможностями приложения.
* В модуле обрабатывается информацию как о картах, так и о счетах, анализирует транзакции клиентов.

## Примеры работы функции
### Результаты сортировки по статусу "Исполенные"
+ id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364
+ id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572


### Результаты сортировки по статусу "Отменненые"
+ id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689
+ id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441


## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/RVV59/Bank
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd [Bank](https://github.com/RVV59/Bank)
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```
