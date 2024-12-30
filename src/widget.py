def mask_card_number(card_number):
    # Пример маскировки номера карты: оставить первые 4 и последние 4 цифры
    return card_number[:4] + '*' * (len(card_number) - 8) + card_number[-4:]

def mask_account_number(account_number):
    # Пример маскировки номера счета: оставить только последние 4 цифры
    return '*' * (len(account_number) - 4) + account_number[-4:]

def mask_account_card(info):
    if info.startswith("Счет"):
        # Маскировка номера счета
        account_number = info.split()[-1]
        return f"Счет {mask_account_number(account_number)}"
    else:
        # Маскировка номера карты
        card_number = info.split()[-1]
        return f"{info.rsplit(' ', 1)[0]} {mask_card_number(card_number)}"


