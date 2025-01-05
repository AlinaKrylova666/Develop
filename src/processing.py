def filter_by_state(transactions, state='EXECUTED'):
    return [transaction for transaction in transactions if transaction["state"] == state]


def sort_by_date(transactions, order=True):
    return sorted(transactions, key=lambda x: x["date"], reverse=order)
