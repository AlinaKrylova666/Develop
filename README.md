## Описание

Цель проекта — предоставить пользователям набор утилит для обработки и анализа транзакций. Основные функции включают фильтрацию транзакций по статусу и сортировку по дате.
Этот проект включает в себя модуль `generators`, который предоставляет функции для работы с транзакциями и генерации номеров банковских карт.
## Установка

Для работы с проектом выполните следующие шаги:

1. Клонируйте репозиторий:
   
   git clone https://github.com/username/transaction-processor.git
   cd transaction-processor
   

2. Установите зависимости:
   Убедитесь, что у вас установлен Python 3.x. Установите необходимые пакеты, если они присутствуют в requirements.txt:
   
   pip install -r requirements.txt
   

## Использование

Ниже представлены примеры использования основных функций проекта.

## Модуль Generators

Модуль `generators` содержит следующие функции:

### `filter_by_currency(transactions, currency)`

Фильтрует список транзакций по указанной валюте.

**Параметры:**
- `transactions`: список словарей, представляющих транзакции.
- `currency`: строка, обозначающая валюту для фильтрации (например, 'USD').

**Возвращает:**
- Итератор, выдающий транзакции с указанной валютой.

**Пример использования:**
```python
transactions = [
    {'id': 1, 'amount': 100, 'currency': 'USD'},
    {'id': 2, 'amount': 200, 'currency': 'EUR'},
    {'id': 3, 'amount': 150, 'currency': 'USD'},
]

filtered_transactions = filter_by_currency(transactions, 'USD')

for transaction in filtered_transactions:
    print(transaction)
```

### `transaction_descriptions(transactions)`

Генерирует описание каждой транзакции.

**Параметры:**
- `transactions`: список словарей, представляющих транзакции.

**Возвращает:**
- Итератор, выдающий строку с описанием каждой транзакции.

**Пример использования:**
```python
transactions = [
    {'id': 1, 'amount': 100, 'currency': 'USD'},
    {'id': 2, 'amount': 200, 'currency': 'EUR'},
    {'id': 3, 'amount': 150, 'currency': 'USD'},
]

for description in transaction_descriptions(transactions):
    print(description)
```

### `card_number_generator(start, end)`

Генерирует номера банковских карт в формате `XXXX XXXX XXXX XXXX`.

**Параметры:**
- `start`: начальное значение (например, 1 для 0000 0000 0000 0001).
- `end`: конечное значение (например, 9999999999999999 для 9999 9999 9999 9999).

**Возвращает:**
- Итератор, выдающий строку с номером карты в указанном формате.

**Пример использования:**
```python
start = 1
end = 10

for card_number in card_number_generator(start, end):
    print(card_number)

### Функция filter_by_state

Фильтрует список транзакций по указанному состоянию, по умолчанию EXECUTED.

from transaction_processor import filter_by_state

transactions = [
    {"id": 1, "state": "EXECUTED", "date": "2023-10-01"},
    {"id": 2, "state": "PENDING", "date": "2023-10-02"}
]

executed_transactions = filter_by_state(transactions)
print(executed_transactions)


### Функция sort_by_date

Сортирует транзакции по дате. По умолчанию сортирует в порядке убывания.

from transaction_processor import sort_by_date

transactions = [
    {"id": 1, "state": "EXECUTED", "date": "2023-10-01"},
    {"id": 2, "state": "PENDING", "date": "2023-10-02"}
]

sorted_transactions = sort_by_date(transactions)
print(sorted_transactions)


## Примеры

1. Фильтрация транзакций:
   
   from transaction_processor import filter_by_state

   transactions = [
       {"id": 1, "state": "EXECUTED", "date": "2023-10-01"},
       {"id": 2, "state": "PENDING", "date": "2023-10-02"}
   ]

   executed_transactions = filter_by_state(transactions)
   print(executed_transactions)  # [{'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01'}]
   

2. Сортировка транзакций:
   
   from transaction_processor import sort_by_date

   transactions = [
       {"id": 1, "state": "EXECUTED", "date": "2023-10-01"},
       {"id": 2, "state": "PENDING", "date": "2023-10-02"}
   ]

   sorted_transactions = sort_by_date(transactions)
   print(sorted_transactions)  # [{'id': 2, 'state': 'PENDING', 'date': '2023-10-02'}, {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01'}]
   

## Вклад

Если вы хотите внести свой вклад в проект, пожалуйста, следуйте этим шагам:

1. Форкните репозиторий.
2. Создайте новую ветку (git checkout -b feature-branch).
3. Внесите свои изменения и зафиксируйте их (git commit -m 'Add new feature').
4. Запушьте изменения в свою ветку (git push origin feature-branch).
5. Откройте Pull Request.

## Тестирование

Этот проект использует `pytest` для написания и выполнения тестов. Следуйте инструкциям ниже, чтобы настроить и запустить тесты.

### Установка Pytest

Если `pytest` еще не установлен, вы можете установить его с помощью pip:


### Запуск тестов

Чтобы запустить все тесты, выполните следующую команду в корневой директории проекта:


Это выполнит все тесты, которые находятся в файлах, начинающихся с `test_` или заканчивающихся на `_test.py`. Вы также можете запустить конкретный тестовый файл:

### Использование фикстур

В проекте используются фикстуры для упрощения тестирования. Фикстуры определены для различных наборов данных, которые используются в тестах, например, для тестирования маскировки номеров карт и счетов, а также для проверки фильтрации и сортировки транзакций по состоянию и дате.


