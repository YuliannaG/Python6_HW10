"""Парсер команд. Часть которая отвечает за разбор введенных пользователем строк,
выделение из строки ключевых слов и модификаторов команд."""
from handler import *


def normalize(raw_user_input: str) -> dict:
    user_input = raw_user_input.lower().strip()
    user_command: dict = {'command': None, 'name': None, 'phone': []}

    if user_input in ['hello', 'show all', 'good buy', 'close', 'exit']:
        user_command['command'] = user_input
    else:
        user_input_list = user_input.split()
        user_command['command'] = user_input_list[0]
        user_command['name'] = user_input_list[1]
        if len(user_input_list) > 2:
            user_command['phone'].append(user_input_list[2])
        if len(user_input_list) > 3:
            user_command['phone'].append(user_input_list[3])

    return user_command


if __name__ == '__main__':
    user_command = normalize('add Maria 44 66')
    name = Name(user_command['name'])
    phone = Phone(user_command['phone'])
    record = Record(name, phone)
    command = user_command['command']
    print(phone)

    print(func_hello())
    print(add_contact(record, name))
    print(contacts_dict)
