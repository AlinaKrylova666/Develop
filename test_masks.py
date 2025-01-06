import pytest
from src.masks import get_mask_card_number, get_mask_account

# Фикстура для тестовых данных карт
@pytest.fixture
def card_numbers():
    return {
        "valid": "1234567812345678",
        "invalid_length": "12345678",
        "valid_with_spaces": "1234 5678 1234 5678"
    }

# Фикстура для тестовых данных счетов
@pytest.fixture
def account_numbers():
    return {
        "valid": "12345678901234567890",
        "invalid_length": "12345678",
        "invalid_characters": "1234567890abcdef1234"
    }

def test_get_mask_card_number_valid(card_numbers):
    expected_result = "1234 56** **** 5678"
    assert get_mask_card_number(card_numbers["valid"]) == expected_result


def test_get_mask_card_number_invalid_length(card_numbers):
    # Ожидается, что функция вернет исходное значение и выведет сообщение об ошибке
    expected_result = card_numbers["invalid_length"]
    assert get_mask_card_number(card_numbers["invalid_length"]) == expected_result

def test_get_mask_account_valid(account_numbers):
    expected_result = "**7890"
    assert get_mask_account(account_numbers["valid"]) == expected_result


def test_get_mask_account_invalid_length(account_numbers):
    # Ожидается, что функция вернет исходное значение и выведет сообщение об ошибке
    expected_result = account_numbers["invalid_length"]
    assert get_mask_account(account_numbers["invalid_length"]) == expected_result

def test_get_mask_account_invalid_characters(account_numbers):
    # Ожидается, что функция вернет исходное значение и выведет сообщение об ошибке
    expected_result = account_numbers["invalid_characters"]
    assert get_mask_account(account_numbers["invalid_characters"]) == expected_result
