def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает ее маску"""

    return f"{card_number[:len(card_number) - 16]} {card_number[-16:-12]} {card_number[-11:-13]}** **** {card_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(input()))
