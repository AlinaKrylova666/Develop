from src.utils import load_transactions

file_path = '../data/transactions.json'
transactions = load_transactions(file_path)

print(transactions)
