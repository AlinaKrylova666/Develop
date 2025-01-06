import pytest
from typing import List, Dict
from src.processing import filter_by_state, sort_by_date  # Замени your_module на имя модуля

# Фикстура для тестовых данных транзакций
@pytest.fixture
def transactions_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01"},
        {"id": 2, "state": "PENDING", "date": "2023-09-30"},
        {"id": 3, "state": "EXECUTED", "date": "2023-10-02"},
        {"id": 4, "state": "CANCELLED", "date": "2023-10-03"},
        {"id": 5, "state": "PENDING", "date": "2023-10-01"},
    ]

def test_filter_by_state_default(transactions_data):
    expected_result = [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01"},
        {"id": 3, "state": "EXECUTED", "date": "2023-10-02"}
    ]
    assert filter_by_state(transactions_data) == expected_result

def test_filter_by_state_custom(transactions_data):
    expected_result = [
        {"id": 2, "state": "PENDING", "date": "2023-09-30"},
        {"id": 5, "state": "PENDING", "date": "2023-10-01"}
    ]
    assert filter_by_state(transactions_data, state="PENDING") == expected_result

def test_filter_by_state_no_matches(transactions_data):
    expected_result = []
    assert filter_by_state(transactions_data, state="FAILED") == expected_result

def test_sort_by_date_descending(transactions_data):
    expected_result = [
        {"id": 4, "date": "2023-10-03", "state": "CANCELLED"},
        {"id": 3, "date": "2023-10-02", "state": "EXECUTED"},
        {"id": 1, "date": "2023-10-01", "state": "EXECUTED"},
        {"id": 5, "date": "2023-10-01", "state": "PENDING"},
        {"id": 2, "date": "2023-09-30", "state": "PENDING"}
    ]
    assert sort_by_date(transactions_data) == expected_result

def test_sort_by_date_ascending(transactions_data):
    expected_result = [
        {"id": 2, "date": "2023-09-30", "state": "PENDING"},
        {"id": 1, "date": "2023-10-01", "state": "EXECUTED"},
        {"id": 5, "date": "2023-10-01", "state": "PENDING"},
        {"id": 3, "date": "2023-10-02", "state": "EXECUTED"},
        {"id": 4, "date": "2023-10-03", "state": "CANCELLED"}
    ]
    assert sort_by_date(transactions_data, order=False) == expected_result
