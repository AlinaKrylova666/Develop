def filter_by_currency(transactions, currency):
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: список словарей, представляющих транзакции
    :param currency: строка, обозначающая валюту для фильтрации (например, 'USD')
    :return: итератор, выдающий транзакции с указанной валютой
    """
    return (transaction for transaction in transactions if transaction.get('currency') == currency)

# Пример использования:
transactions = [
    {'id': 1, 'amount': 100, 'currency': 'USD'},
    {'id': 2, 'amount': 200, 'currency': 'EUR'},
    {'id': 3, 'amount': 150, 'currency': 'USD'},
]

filtered_transactions = filter_by_currency(transactions, 'USD')

for transaction in filtered_transactions:
    print(transaction)

