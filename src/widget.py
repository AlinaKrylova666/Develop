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



from datetime import datetime

def get_date(date_string):
    # Парсим строку с датой в объект datetime
    date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    # Возвращаем строку в нужном формате
    return date_object.strftime("%d.%m.%Y")

# Пример использования:
print(get_date("2024-03-11T02:26:18.671407"))