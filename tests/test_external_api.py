import unittest
from unittest.mock import patch
from src.external_api import convert_transaction_to_rub


class TestCurrencyConversion(unittest.TestCase):

    @patch('src.external_api.requests.get')
    def test_convert_usd_to_rub(self, mock_get):
        # Mocking the API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "result": 75000.0  # Example conversion result
        }

        transaction = {
            "operationAmount": {
                "amount": "1000",
                "currency": {
                    "name": "доллар",
                    "code": "USD"
                }
            }
        }

        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 75000.0)

    @patch('src.external_api.requests.get')
    def test_convert_eur_to_rub(self, mock_get):
        # Mocking the API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "result": 90000.0  # Example conversion result
        }

        transaction = {
            "operationAmount": {
                "amount": "1000",
                "currency": {
                    "name": "евро",
                    "code": "EUR"
                }
            }
        }

        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 90000.0)

    def test_convert_rub_to_rub(self):
        transaction = {
            "operationAmount": {
                "amount": "1000",
                "currency": {
                    "name": "рубль",
                    "code": "RUB"
                }
            }
        }

        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 1000.0)


if __name__ == '__main__':
    unittest.main()
