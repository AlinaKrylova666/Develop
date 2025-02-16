from utils import load_transactions

file_path = 'data/operations.json'
transactions = load_transactions(file_path)

print(transactions)
