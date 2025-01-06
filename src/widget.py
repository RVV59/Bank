
def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает ее маску"""

    return f"{card_number[:len(card_number) - 16]} {card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:
    ]}"


def get_mask_account(card_mask: str) -> str:
    """принимает номер счета и возвращает его маску"""

    return f"{card_mask[:len(card_mask) - 20]} **{card_mask[-4:]}"


def get_date(date: str) -> str:
    """замена формата даты на краткий дд.мм.гггг"""

    new_date = date[:10].split('-')
    return '.'.join(new_date[::-1])


if __name__ == "__main__":
    print(get_mask_card_number(input()))
    print(get_mask_account(input()))
    print(get_date(input()))
