from src.external_api import get_exchange_rate


def convert_transaction_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Аргументы:
        transaction (dict): Словарь с информацией о транзакции, содержащий ключи 'amount' и 'currency'.

    Возвращает:
        float: Сумма транзакции в рублях.
    """
    amount = transaction['amount']
    currency = transaction['currency']

    if currency == 'RUB':
        return float(amount)

    try:
        rate = get_exchange_rate(currency)
        return float(amount) * rate
    except Exception as e:
        raise ValueError(f"Error converting currency: {e}")
