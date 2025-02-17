from src.external_api import get_exchange_rate

def convert_transaction_to_rub(transaction):
    amount = transaction['amount']
    currency = transaction['currency']

    if currency == 'RUB':
        return float(amount)

    rate = get_exchange_rate(currency)
    return float(amount) * rate
