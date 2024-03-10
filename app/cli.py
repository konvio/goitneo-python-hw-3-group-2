import datetime
from app.bdays import get_next_week_bdays
from app.model import AddressBook
from app.decorators import args_len, handle_errors
import app.config as config

data = AddressBook()

@args_len(2)
@handle_errors
def add(*args):
    name, phone = args
    data.add_contact(name, phone)
    print(f"Added {name} with phone number {phone}")


@args_len(2)
@handle_errors
def change(*args):
    name, phone = args
    data.change_contact(name, phone=phone)
    print(f"Changed {name} phone to {phone}")


@args_len(1)
@handle_errors
def phone(name):
    print(f"Phone number for {name} is {data[name].phone}")

@args_len(2)
@handle_errors
def add_birthday(*args):
    name, bday_str = args

    bday = datetime.datetime.strptime(bday_str, config.DATE_FORMAT).date()
    data[name].birthday = bday

    print(f"Added {name} with birthday {bday.strftime(config.DATE_FORMAT)}")

@args_len(1)
@handle_errors
def show_birthday(name):
    print(f"Birthday for {name} is {data[name].birthday.strftime(config.DATE_FORMAT)}")

@args_len(0)
@handle_errors
def birthdays():
    names = get_next_week_bdays(data.values())
    if len(names) == 0:
        print("No birthdays in the next week")
        return
    for name in names:
        print(f"{name} has a birthday on {name[0].strftime(config.DATE_FORMAT)}")

@args_len(0)
@handle_errors
def all():
    if len(data) == 0:
        print("The address book is empty")
        return
    for name, contact in data.items():
        print(f"{name}: {contact.phone}")

commands = {
    "hello": lambda: print("How can I help you?"),
    "help": lambda: print("Available commands: add, change, phone, add-birthday, show-birthday, birthdays, all, exit"),
    "add": add,
    "change": change,
    "phone": phone,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
    "all": all,
}

def start():
    print("Welcome to the assistant bot! Type 'help' to see available commands.")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse(user_input)

        if command == "exit":
            print("Good bye!")
            break

        if command in commands:
            commands[command](*args)
        else:
            print("Invalid command. Type 'help' to see available commands.")

def parse(input: str) -> tuple[str, list[str]]:
    cmd, *args = input.strip().lower().split()
    return cmd, args
