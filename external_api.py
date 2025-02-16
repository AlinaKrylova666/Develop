import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем API ключ из переменных окружения
API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')


def get_exchange_rate(from_currency, to_currency='RUB'):
    """
    Получает курс обмена между двумя валютами.

    :param from_currency: Валюта, из которой конвертируем (например, 'USD' или 'EUR')
    :param to_currency: Валюта, в которую конвертируем (по умолчанию 'RUB')
    :return: Курс обмена
    """
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={from_currency}&symbols={to_currency}"
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Проверяем, нет ли ошибок в запросе

    data = response.json()
    return data['rates'][to_currency]
