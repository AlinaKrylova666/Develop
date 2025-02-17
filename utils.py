from src.logs.logging_setup import setup_logger

# Настройка логгера для utils
logger = setup_logger('utils', 'logs/utils.log')

def load_transactions(file_path):
    if not os.path.exists(file_path):
        logger.warning(f"File not found: {file_path}")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Loaded {len(data)} transactions from {file_path}")
                return data
            else:
                logger.warning(f"Data in file {file_path} is not a list")
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error in file {file_path}: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred while loading transactions from {file_path}: {e}")

    return []

if __name__ == "__main__":
    # Пример тестового вызова функции
    load_transactions('data/operations.json')


import pandas as pd
import json
import os
from src.logs.logging_setup import setup_logger

# Настройка логгера для utils
logger = setup_logger('utils', 'logs/utils.log')

def load_transactions_from_json(file_path):
    if not os.path.exists(file_path):
        logger.warning(f"File not found: {file_path}")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Loaded {len(data)} transactions from {file_path}")
                return data
            else:
                logger.warning(f"Data in file {file_path} is not a list")
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error in file {file_path}: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred while loading transactions from {file_path}: {e}")

    return []

def load_transactions_from_csv(file_path):
    if not os.path.exists(file_path):
        logger.warning(f"File not found: {file_path}")
        return []

    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient='records')
        logger.info(f"Loaded {len(transactions)} transactions from {file_path}")
        return transactions
    except Exception as e:
        logger.error(f"An error occurred while loading transactions from CSV file {file_path}: {e}")
        return []

def load_transactions_from_xlsx(file_path):
    if not os.path.exists(file_path):
        logger.warning(f"File not found: {file_path}")
        return []

    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient='records')
        logger.info(f"Loaded {len(transactions)} transactions from {file_path}")
        return transactions
    except Exception as e:
        logger.error(f"An error occurred while loading transactions from XLSX file {file_path}: {e}")
        return []

if __name__ == "__main__":
    # Пример использования функций
    json_transactions = load_transactions_from_json('data/transactions.json')
    csv_transactions = load_transactions_from_csv('data/transactions.csv')
    xlsx_transactions = load_transactions_from_xlsx('data/transactions_excel.xlsx')

    print(f"JSON Transactions: {json_transactions}")
    print(f"CSV Transactions: {csv_transactions}")
    print(f"XLSX Transactions: {xlsx_transactions}")
