def get_mask_card_number(card_number: str) -> str:

    return f"{card_number[:len(card_number) - 12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(card_mask: str) -> str:

    return f"**{card_mask[-4:]}"


def get_date(date: str) -> str:

    new_date = date[:10].split('-')
    return '.'.join(new_date[::-1])


if __name__ == "__main__":
    print(get_mask_card_number(input().strip()))
    print(get_mask_account(input().strip()))
    print(get_date(input().strip()))
