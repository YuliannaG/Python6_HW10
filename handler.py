"""Функции обработчики команд -- набор функций, которые ещё называют handler,
они отвечают за непосредственное выполнение команд."""
from collections import UserDict



class Field():
    ...


class Name(Field):

    def __init__(self, name: str):
        self.name = name


    def __repr__(self):
        return f'{self.name}'


class Phone(Field):
    def __init__(self, phone: str):
        self.phone = phone


    def __repr__(self):
        return f'{self.phone}'


class Record(UserDict):

    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        #self.data = {self.name: self.phone}


    def __repr__(self):
        return f'{self.name.name} : {[p.phone for p in self.phones]}'

    def add_phone(self, phone: Phone):
        if phone.phone not in [p.phone for p in self.phones]:
            self.phones.append(phone)
            return phone
    
    def delete_phone(self, phone: Phone):
        for p in self.phones:
            if p.phone == phone.phone:
                self.phones.remove(p)
                return phone
    
    def change_phone(self, phone: Phone, new_phone:Phone):
        if self.delete_phone(phone):
            self.add_phone(new_phone)
            return phone, new_phone


class AddressBook(UserDict):

    # def __init__(self):
    #     self.data = {}

    def add_record(self, record: Record):
        self.data[record.name.name] = record


contacts_dict = AddressBook()


def func_hello(*args):
    return "How can I help you?"


def add_contact(name, phone):
    name_a = Name(name)
    phone_a = Phone(phone)
    record_a = Record(name_a, phone_a)
    contacts_dict.add_record(record_a)
    return f'Contact {str(name_a).capitalize()} added'


def change_contact(name, phone, new_phone):
    record = contacts_dict.get(name) #Record(contacts_dict[name])
    print(type(record))
    if isinstance(record, Record):
        record.change_phone(Phone(phone), Phone(new_phone))
        return f'Contact {name} changed number {phone} to number {new_phone}'
    return f'Sorry, phone book has no entry with name {name}'

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
    print(name)
    phone = Phone('444')
    print(phone)
    record = Record(name, phone)
    print(record)
    print(func_hello())
    print(add_contact('Mariya', '1238495'))
    print(contacts_dict)
    print(change_contact('Mariya','1238495', '3456'))
    print(contacts_dict)