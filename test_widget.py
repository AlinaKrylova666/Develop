import pytest
from src.widget import mask_card_number, mask_account_number, mask_account_card, get_date

# Фикстура для номеров карт
@pytest.fixture
def card_numbers():
    return {
        "valid": "1234567812345678",
        "short": "1234",
        "long": "12345678901234567890"
    }

# Фикстура для номеров счетов
@pytest.fixture
def account_numbers():
    return {
        "valid": "12345678901234567890",
        "short": "1234",
        "with_letters": "1234abc7890123456789"
    }

# Фикстура для строк с датами
@pytest.fixture
def date_strings():
    return {
        "valid": "2023-10-05T14:48:00.000",
        "invalid": "05-10-2023"
    }

def test_mask_card_number(card_numbers):
    assert mask_card_number(card_numbers["valid"]) == "1234********5678"
    assert mask_card_number(card_numbers["short"]) == "1234"
    assert mask_card_number(card_numbers["long"]) == "1234************7890"  # 12 звездочек

def test_mask_account_number(account_numbers):
    assert mask_account_number(account_numbers["valid"]) == "****************7890"
    assert mask_account_number(account_numbers["short"]) == "**34"
    assert mask_account_number(account_numbers["with_letters"]) == "****************6789"

def test_mask_account_card(card_numbers, account_numbers):
    assert mask_account_card(f"Счет {account_numbers['valid']}") == "Счет ****************7890"
    assert mask_account_card(f"Карта VISA {card_numbers['valid']}") == "Карта VISA 1234********5678"

def test_get_date(date_strings):
    assert get_date(date_strings["valid"]) == "05.10.2023"
    with pytest.raises(ValueError):
        get_date(date_strings["invalid"])
