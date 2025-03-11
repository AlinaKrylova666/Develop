import json
import csv
from openpyxl import load_workbook
from transaction_utils import filter_transactions_by_description, count_transactions_by_category

def load_transactions_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_transactions_from_csv(file_path):
    transactions = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(row)
    return transactions

def load_transactions_from_xlsx(file_path):
    workbook = load_workbook(filename=file_path)
    sheet = workbook.active
    transactions = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        transactions.append({
            "date": row[0],
            "description": row[1],
            "account": row[2],
            "amount": row[3],
            "currency": row[4],
            "status": row[5]
        })
    return transactions

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ")
    if choice == "1":
        transactions = load_transactions_from_json('data/transactions.json')
    elif choice == "2":
        transactions = load_transactions_from_csv('data/transactions.csv')
    elif choice == "3":
        transactions = load_transactions_from_xlsx('data/transactions.xlsx')
    else:
        print("Неверный выбор.")
        return

    print("Для обработки выбран JSON-файл.")

    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")
        if status.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            filtered_transactions = [t for t in transactions if t['status'].upper() == status.upper()]
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    sort_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_choice == 'да':
        order_choice = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        reverse = order_choice == 'по убыванию'
        filtered_transactions.sort(key=lambda x: x['date'], reverse=reverse)

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if currency_choice == 'да':
        filtered_transactions = [t for t in filtered_transactions if t['currency'].upper() == 'RUB']

    description_filter_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    if description_filter_choice == 'да':
        search_string = input("Введите слово для фильтрации по описанию:\n")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(f"{transaction['date']} {transaction['description']}")
            print(f"Счет {transaction['account']}")
            print(f"Сумма: {transaction['amount']} {transaction['currency']}")


if __name__ == "__main__":
    main()


