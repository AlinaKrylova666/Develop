def transaction_descriptions(transactions):
    """
    Генератор, возвращающий описание каждой транзакции.

    :param transactions: список словарей, представляющих транзакции
    :yield: строка с описанием транзакции
    """
    for transaction in transactions:
        description = f"Transaction ID: {transaction.get('id')}, Amount: {transaction.get('amount')}, Currency: {transaction.get('currency')}"
        yield description

# Пример использования:
transactions = [
    {'id': 1, 'amount': 100, 'currency': 'USD'},
    {'id': 2, 'amount': 200, 'currency': 'EUR'},
    {'id': 3, 'amount': 150, 'currency': 'USD'},
]

for description in transaction_descriptions(transactions):
    print(description)


def card_number_generator(start, end):
    """
    Генератор, выдающий номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение (например, 1 для 0000 0000 0000 0001)
    :param end: конечное значение (например, 9999999999999999 для 9999 9999 9999 9999)
    :yield: строка с номером карты в формате XXXX XXXX XXXX XXXX
    """
    for number in range(start, end + 1):
        # Преобразуем число в строку с ведущими нулями до 16 символов
        card_number = f"{number:016}"
        # Форматируем строку в виде XXXX XXXX XXXX XXXX
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number

# Пример использования:
start = 1
end = 10  # Для демонстрации небольшой диапазон

for card_number in card_number_generator(start, end):
    print(card_number)
