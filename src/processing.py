from typing import List, Dict

def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список транзакций по их состоянию.

    Аргументы:
        transactions (List[Dict]): Список словарей транзакций.
        state (str): Состояние, по которому необходимо фильтровать транзакции. По умолчанию 'EXECUTED'.

    Возвращает:
        List[Dict]: Список транзакций с указанным состоянием.
    """
    return [transaction for transaction in transactions if transaction["state"] == state]


def sort_by_date(transactions: List[Dict], order: bool = True) -> List[Dict]:
    """
    Сортирует список транзакций по дате.

    Аргументы:
        transactions (List[Dict]): Список словарей транзакций.
        order (bool): Если True, сортирует транзакции в порядке убывания.
                      Если False, сортирует в порядке возрастания. По умолчанию True.

    Возвращает:
        List[Dict]: Список транзакций, отсортированных по дате.
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=order)
