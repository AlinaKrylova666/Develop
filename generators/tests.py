import unittest

from home import filter_by_currency


class TestFilterByCurrency(unittest.TestCase):

    def test_filter_by_currency(self):
        transactions = [
            {'id': 1, 'amount': 100, 'currency': 'USD'},
            {'id': 2, 'amount': 200, 'currency': 'EUR'},
            {'id': 3, 'amount': 150, 'currency': 'USD'},
        ]

        # Тестирование фильтрации по валюте USD
        result = list(filter_by_currency(transactions, 'USD'))
        expected = [
            {'id': 1, 'amount': 100, 'currency': 'USD'},
            {'id': 3, 'amount': 150, 'currency': 'USD'},
        ]
        self.assertEqual(result, expected)

        # Тестирование фильтрации по валюте, которая отсутствует
        result = list(filter_by_currency(transactions, 'GBP'))
        self.assertEqual(result, [])

        # Тестирование фильтрации по валюте EUR
        result = list(filter_by_currency(transactions, 'EUR'))
        expected = [
            {'id': 2, 'amount': 200, 'currency': 'EUR'},
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

import unittest

from generator import transaction_descriptions, card_number_generator


class TestGenerators(unittest.TestCase):

    def test_transaction_descriptions(self):
        transactions = [
            {'id': 1, 'amount': 100, 'currency': 'USD'},
            {'id': 2, 'amount': 200, 'currency': 'EUR'},
            {'id': 3, 'amount': 150, 'currency': 'USD'},
        ]

        result = list(transaction_descriptions(transactions))
        expected = [
            "Transaction ID: 1, Amount: 100, Currency: USD",
            "Transaction ID: 2, Amount: 200, Currency: EUR",
            "Transaction ID: 3, Amount: 150, Currency: USD",
        ]
        self.assertEqual(result, expected)

    def test_card_number_generator(self):
        start = 1
        end = 3
        result = list(card_number_generator(start, end))
        expected = [
            '0000 0000 0000 0001',
            '0000 0000 0000 0002',
            '0000 0000 0000 0003',
        ]
        self.assertEqual(result, expected)

        # Тестирование генерации с крайними значениями
        start = 9999999999999999
        end = 9999999999999999
        result = list(card_number_generator(start, end))
        expected = ['9999 9999 9999 9999']
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
