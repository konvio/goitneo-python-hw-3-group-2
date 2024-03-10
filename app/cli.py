from app.model import AddressBook
from app.decorators import args_len, handle_errors

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
    print(data[name].phone)



@handle_errors
def all():
    if len(data) == 0:
        print("The address book is empty")
        return
    for name, contact in data.items():
        print(f"{name}: {contact.phone}")

commands = {
    "hello": lambda: print("How can I help you?"),
    "add": add,
    "change": change,
    "phone": phone,
    "all": all,
}

def start():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command [hello,add,change,phone,all,exit]: ")
        command, args = parse(user_input)

        if command == "exit":
            print("Good bye!")
            break

        if command in commands:
            commands[command](*args)
        else:
            print("Invalid command")

def parse(input: str) -> tuple[str, list[str]]:
    cmd, *args = input.strip().lower().split()
    return cmd, args
