from src.logs.logging_setup import setup_logger

# Настроить логгер для masks
logger = setup_logger('masks', 'logs/masks.log')


def get_mask_card_number(card_number):
    """Маскирует номер банковской карты, оставляя видимыми только последние 4 цифры."""
    try:
        if len(card_number) < 4:
            raise ValueError("Card number is too short to mask")

        masked_number = '*' * (len(card_number) - 4) + card_number[-4:]
        logger.info(f"Card number masked successfully: {masked_number}")
        return masked_number
    except Exception as e:
        logger.error(f"An error occurred while masking card number: {e}")
        return None


def get_mask_account(account_number):
    """Маскирует номер банковского счета, оставляя видимыми только последние 4 символа."""
    try:
        if len(account_number) < 4:
            raise ValueError("Account number is too short to mask")

        masked_account = '*' * (len(account_number) - 4) + account_number[-4:]
        logger.info(f"Account number masked successfully: {masked_account}")
        return masked_account
    except Exception as e:
        logger.error(f"An error occurred while masking account number: {e}")
        return None


if __name__ == "__main__":
    # Пример использования функции
    card_number = "1234567812345678"
    print(get_mask_card_number(card_number))  # Вывод: ************5678

    account_number = "1234567890123456"
    print(get_mask_account(account_number))  # Вывод: ************3456
