import unittest
from unittest.mock import patch
from transaction_processor import convert_transaction_to_rub

class TestTransactionProcessor(unittest.TestCase):

    @patch('external_api.get_exchange_rate')
    def test_convert_transaction_usd_to_rub(self, mock_get_exchange_rate):
        mock_get_exchange_rate.return_value = 75.0
        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_transaction_to_rub(transaction)
        expected_result = 100 * 75.0
        self.assertEqual(result, expected_result)

    def test_convert_transaction_rub(self):
        transaction = {'amount': 1000, 'currency': 'RUB'}
        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 1000.0)

if __name__ == '__main__':
    unittest.main()
