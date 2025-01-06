from datetime import datetime


def mask_card_number(card_number: str) -> str:
    """Маскировка номера карты: оставить первые 4 и последние 4 цифры"""
    if len(card_number) > 8:
        return card_number[:4] + '*' * (len(card_number) - 8) + card_number[-4:]
    return card_number


def mask_account_number(account_number: str) -> str:
    """Маскировка номера счета: оставить только последние 4 цифры"""
    length = len(account_number)
    if length > 4:
        return '*' * (length - 4) + account_number[-4:]
    return '*' * (length - 2) + account_number[-2:]



def mask_account_card(info: str) -> str:
    if info.startswith("Счет"):
        """Маскировка номера счета"""
        account_number = info.split()[-1]
        return f"Счет {mask_account_number(account_number)}"
    else:
        """Маскировка номера карты"""
        card_number = info.split()[-1]
        # Здесь добавим обработку на случай некорректного номера
        if len(card_number) >= 8:
            return f"{info.rsplit(' ', 1)[0]} {mask_card_number(card_number)}"
        else:
            # Маскировка для короткого номера
            return f"{info.rsplit(' ', 1)[0]} {'*' * (len(card_number) - 2)}{card_number[-2:]}"



def get_date(date_string: str) -> str:
    """Парсим строку с датой в объект datetime"""
    date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    """Возвращаем строку в нужном формате"""
    return date_object.strftime("%d.%m.%Y")
