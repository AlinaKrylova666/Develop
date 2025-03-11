import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card
from src.widget import get_date
from src.processing import filter_by_state


def test_get_mask_card_number_valid():
    card_number = "1234567812345678"
    expected_result = "1234********5678"
    assert get_mask_card_number(card_number) == expected_result


def test_get_mask_card_number_invalid():
    card_number = "12345678"
    expected_result = "12345678"  # Ожидаемое значение при ошибке
    assert get_mask_card_number(card_number) == expected_result


def test_get_mask_account_valid():
    account_number = "12345678901234567890"
    expected_result = "****************7890"
    assert get_mask_account(account_number) == expected_result


def test_get_mask_account_invalid_length():
    account_number = "12345678901234567"
    expected_result = "***********4567"
    assert get_mask_account(account_number) == expected_result


def test_mask_account_card_with_account():
    info = "Счет 12345678901234567890"
    expected_result = "Счет ****************7890"
    assert mask_account_card(info) == expected_result


def test_mask_account_card_with_card():
    info = "Карта VISA 1234567812345678"
    expected_result = "Карта VISA 1234********5678"
    assert mask_account_card(info) == expected_result


def test_get_date():
    date_string = "2023-10-05T14:48:00.000"
    expected_result = "05.10.2023"
    assert get_date(date_string) == expected_result


def test_get_date_invalid_format():
    with pytest.raises(ValueError):
        get_date("05-10-2023")


def test_filter_by_state_default():
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
    transactions = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"}
    ]
    expected_result = [
        {"id": 2, "state": "PENDING"}
    ]
    assert filter_by_state(transactions, state="PENDING") == expected_result
