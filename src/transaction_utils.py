import re

def filter_transactions_by_description(transactions, search_string):
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction['description'])]

def count_transactions_by_category(transactions, categories):
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        for category in categories:
            if category.lower() in transaction['description'].lower():
                category_count[category] += 1
    return category_count