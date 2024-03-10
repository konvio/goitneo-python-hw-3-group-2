from collections import UserDict, UserList
from dataclasses import dataclass
import datetime

import app.validation as validation

@dataclass
class Contact:
    name: str
    phone: str
    birthday: datetime.date


class AddressBook(UserDict[str, Contact]):

    def add_contact(self, name: str, phone: str = None, birthday: datetime.date = None):
        if name in self.data:
            raise ValueError(f"{name} already exists")
        
        self.data[name] = Contact(name, phone, birthday)

    def change_contact(self, name: str, phone: str = None, birthday: datetime.date = None):
        
        contact = self.data[name]

        if phone:
            contact.phone = phone

        if birthday:
            contact.birthday = birthday
