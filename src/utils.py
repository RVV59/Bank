import os
import json


def get_operations_data():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(project_root, 'data', 'operations.json')

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            if isinstance(data, list):
                return data
            else:
                print("Файл содержит данные не в формате списка.")
                return []
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
        return []

# res = get_operations_data()
# print(res)
