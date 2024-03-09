from collections import UserDict, UserList
from dataclasses import dataclass

import app.validation as validation


@dataclass
class Phone:

    value: str

    def __post_init__(self):
        validation.validate_phone(self.value)


class Record(UserList[Phone]):

    name: str

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def add_phone(self, phone: str):
        self.append(Phone(phone))

    def remove_phone(self, phone: str):
        self.remove(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone: str) -> Phone | None:
        return Phone(phone) if Phone(phone) in self else None

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self[record.name] = record

    def find(self, name: str):
        return self[name]

    def delete(self, name: str):
        del self[name]
