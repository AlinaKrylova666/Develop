def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    if len(card_number) != 16:
        print("Неверный формат номера карты")
        return card_number

    mask_card_number = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"
    return mask_card_number


def get_mask_account(card_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    if not (card_number.isdigit() and len(card_number) == 20):
        print("Неверный формат номера счета")
        return card_number

    mask_card_number = f"**{card_number[-4:]}"
    return mask_card_number
