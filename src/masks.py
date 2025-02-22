import os
import logging


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',)
log_dir = os.path.join(project_root, 'logs')
os.makedirs(log_dir, exist_ok=True)
file_handler = logging.FileHandler(os.path.join(log_dir, 'masks.log'), mode='w', encoding='utf-8')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маска номера карты"""
    # if len(card_number) != 16 or card_number == '' or not card_number.isdigit():
    #     logger.error('Неверный номер карты: %s', card_number)
    #     raise ValueError('Номер карты должен состоять из 16 цифр',)
    masked_number = f"{card_number[:- 12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    # masked_number = f"{card_number[:len(card_number) - 12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    logger.info('Получена маска номера карты: %s', masked_number)
    return masked_number


def get_mask_account(card_mask: str) -> str:
    """Маска счета"""
    # if len(card_mask) != 20 or card_mask == '' or not card_mask.isdigit():
    #     logger.error('Неверный номер маски карты: %s', card_mask)
    #     raise ValueError('Номер карты должен состоять из 20 цифр')
    masked_account = f"**{card_mask[-4:]}"
    masked_account = f"Счет **{card_mask[-4:]}"
    logger.info('Получена маска счета: %s', masked_account)
    return masked_account


def get_date(date: str) -> str:
    """Преобразование формата даты"""
    if len(date) != 26 or date == '':
        logger.error('Неверный формат даты: %s', date)
        raise ValueError('Неправильный формат даты')
    new_date = date[:10].split('-')
    formatted_date = '.'.join(new_date[::-1])
    logger.info('Дата преобразована: %s', formatted_date)
    return formatted_date




if __name__ == "__main__":
    print(get_mask_card_number(input()))
    print(get_mask_account(input()))
    print(get_date(input()))
