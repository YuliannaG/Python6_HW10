"""Функции обработчики команд -- набор функций, которые ещё называют handler,
они отвечают за непосредственное выполнение команд."""
from collections import UserDict, UserList



class Field():
    ...


class Name(Field):

    def __init__(self, name: str):
        self.name = name


    def __repr__(self):
        return f'{self.name}'


class Phone(Field):
    def __init__(self, phone: list):
        self.phone: list = phone


    def __repr__(self):
        return f'{self.phone}'


class Record(UserDict):

    def __init__(self, name: Name, phone: Phone):
        self.name = name
        self.phone = phone
        self.data = {self.name: self.phone}


    def __repr__(self):
        return f'{self.data}'


    def change_phone(self, phone: Phone):
        self.phone.remove(phone[0])
        self.phone.append(phone[1])


    def delete_phone(self, phone: Phone):
        self.phone.remove(phone[0])


    def add_phone(self, phone: Phone):
        self.phone.append(phone[0])


class AddressBook(UserDict):

    def __init__(self):
        self.data = {}

    def add_record(self,record: Record):
        self.data[record.name] = record


contacts_dict = AddressBook(UserDict)


def func_hello(*args):
    return "How can I help you?"


def add_contact(name, phone):
    name_a: str = Name(name)
    phone_a = Phone(phone)
    record_a = Record(name,phone)
    contacts_dict.add_record(record_a)
    return f'Contact {str(name_a).capitalize()} added'


def change_contact(name, phone):
    record = Record(contacts_dict[name])
    record.change_phone(phone)
    return f'Contact {name} changed to {phone[1]}'


def phone_contact(name, *args):
    return f"{name}'s number is {contacts_dict[name][name]}"


def show_all(*args):
    # for k,v in contacts_dict.items():
    #     return '{:^10}{:^10}'.format(k, v)
    return contacts_dict


def func_exit(*args):
    return 'Good bye!'


if __name__ == '__main__':
    name = Name('Maria')
    phone = Phone('444')
    record = Record(name, phone)
    print(func_hello())
    print(add_contact(record, name))
    print(contacts_dict)