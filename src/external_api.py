import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_transaction_to_rub(transaction):
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return amount

    params = {
        'from': currency,
        'to': 'RUB',
        'amount': amount,
    }

    headers = {
        'apikey': API_KEY
    }

    response = requests.get(API_URL, headers=headers, params=params)
    response_data = response.json()

    if response.status_code == 200:
        return float(response_data.get('result', 0))
    else:
        raise Exception(f"Error fetching exchange rate: {response_data.get('error', 'Unknown error')}")
