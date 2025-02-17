import json
import os
import logging


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',)
log_dir = os.path.join(project_root, 'logs')
os.makedirs(log_dir, exist_ok=True)
file_handler = logging.FileHandler(os.path.join(log_dir, 'utils.log'), mode='w', encoding='utf-8')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_operations_data():
    '''
    принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    '''
    file_path = os.path.join(project_root, 'data', 'operations.json')

    logger.debug('Попытка открыть файл')

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            if isinstance(data, list):
                logger.info('Успешная загрузка данных из файла')
                return data
            else:
                logger.warning('Файл содержит данные не в формате списка')
                return []
    except FileNotFoundError:
        logger.error('Файл не найден')
        return []
    except json.JSONDecodeError:
        logger.error('Ошибка декодирования JSON-файла')
        return []