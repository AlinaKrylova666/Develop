import pytest
from src.masks import get_mask_card_number

def test_get_mask_card_number_valid():
    # Тестирование корректного номера карты
    card_number = "1234567812345678"
    expected_result = "1234 56** **** 5678"
    assert get_mask_card_number(card_number) == expected_result

def test_get_mask_card_number_invalid():
    # Тестирование некорректного номера карты (меньше 16 цифр)
    card_number = "12345678"
    expected_result = "12345678"  # Так как функция возвращает оригинал при ошибке
    assert get_mask_card_number(card_number) == expected_result

def test_get_mask_card_number_invalid_format():
    # Тестирование некорректного номера карты (больше 16 цифр)
    card_number = "12345678123456789"
    expected_result = "12345678123456789"  # Так как функция возвращает оригинал при ошибке
    assert get_mask_card_number(card_number) == expected_result


import pytest
from src.masks import get_mask_account

def test_get_mask_account_valid():
    # Тестирование корректного номера счета
    account_number = "12345678901234567890"
    expected_result = "**7890"
    assert get_mask_account(account_number) == expected_result

def test_get_mask_account_invalid_length():
    # Тестирование некорректного номера счета (меньше 20 цифр)
    account_number = "12345678901234567"
    expected_result = "12345678901234567"  # Ожидаемое значение при ошибке
    assert get_mask_account(account_number) == expected_result

def test_get_mask_account_invalid_characters():
    # Тестирование некорректного номера счета (содержащего нецифровые символы)
    account_number = "1234567890abcdef1234"
    expected_result = "1234567890abcdef1234"  # Ожидаемое значение при ошибке
    assert get_mask_account(account_number) == expected_result

def test_get_mask_account_invalid_length_and_characters():
    # Тестирование некорректного номера счета (неверная длина и нецифровые символы)
    account_number = "123abc"
    expected_result = "123abc"  # Ожидаемое значение при ошибке
    assert get_mask_account(account_number) == expected_result


import pytest
from src.widget import mask_account_card

def test_mask_account_card_with_account():
    # Тестирование маскировки информации с номером счета
    info = "Счет 12345678901234567890"
    expected_result = "Счет ****************7890"
    assert mask_account_card(info) == expected_result

def test_mask_account_card_with_card():
    # Тестирование маскировки информации с номером карты
    info = "Карта VISA 1234567812345678"
    expected_result = "Карта VISA 1234********5678"
    assert mask_account_card(info) == expected_result

def test_mask_account_card_with_invalid_info():
    # Тестирование обработки некорректной информации
    info = "Неверный формат 1234"
    expected_result = "Неверный формат **34"
    assert mask_account_card(info) == expected_result


import pytest
from datetime import datetime
from src.widget import get_date

def test_get_date():
    # Тестирование корректного преобразования строки даты
    date_string = "2023-10-05T14:48:00.000"
    expected_result = "05.10.2023"
    assert get_date(date_string) == expected_result

def test_get_date_invalid_format():
    # Тестирование обработки некорректного формата даты
    with pytest.raises(ValueError):
        get_date("05-10-2023")


import pytest
from typing import List, Dict
from src.processing import filter_by_state

def test_filter_by_state_default():
    # Тестирование фильтрации с состоянием по умолчанию 'EXECUTED'
    transactions = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"}
    ]
    expected_result = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"}
    ]
    assert filter_by_state(transactions) == expected_result

def test_filter_by_state_custom():
    # Тестирование фильтрации с заданным состоянием 'PENDING'
    transactions = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"}
    ]
    expected_result = [
        {"id": 2, "state": "PENDING"}
    ]
    assert filter_by_state(transactions, state="PENDING") == expected_result

def test_filter_by_state_no_matches():
    # Тестирование фильтрации, когда нет совпадений
    transactions = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"}
    ]
    expected_result = []
    assert filter_by_state(transactions, state="CANCELLED") == expected_result


import pytest
from typing import List, Dict
from src.processing import sort_by_date

def test_sort_by_date_descending():
    # Тестирование сортировки по убыванию по умолчанию
    transactions = [
        {"id": 1, "date": "2023-10-01"},
        {"id": 2, "date": "2023-09-30"},
        {"id": 3, "date": "2023-10-02"}
    ]
    expected_result = [
        {"id": 3, "date": "2023-10-02"},
        {"id": 1, "date": "2023-10-01"},
        {"id": 2, "date": "2023-09-30"}
    ]
    assert sort_by_date(transactions) == expected_result

def test_sort_by_date_ascending():
    # Тестирование сортировки по возрастанию
    transactions = [
        {"id": 1, "date": "2023-10-01"},
        {"id": 2, "date": "2023-09-30"},
        {"id": 3, "date": "2023-10-02"}
    ]
    expected_result = [
        {"id": 2, "date": "2023-09-30"},
        {"id": 1, "date": "2023-10-01"},
        {"id": 3, "date": "2023-10-02"}
    ]
    assert sort_by_date(transactions, order=False) == expected_result

def test_sort_by_date_empty():
    # Тестирование сортировки пустого списка
    transactions = []
    expected_result = []
    assert sort_by_date(transactions) == expected_result


