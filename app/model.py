from collections import UserDict, UserList
from dataclasses import dataclass, field
import datetime

import app.validation as validation

@dataclass
class Contact:
    name: str
    phone: str
    birthday: datetime.date

    def __setattr__(self, prop, val):
        if prop == "phone":
            validation.validate_phone(val)
        super().__setattr__(prop, val)


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
