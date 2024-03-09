from app.model import AddressBook, Record
from app.validation import args_num, input_error

book = AddressBook()


def parse_input(user_input: str) -> tuple[str, list[str]]:
    cmd, *args = user_input.strip().lower().split()
    return cmd, args


@args_num(2)
@input_error
def add_contact(*args):
    name, phone = args

    if name not in book:
        book.add_record(Record(name))
   
    book[name].add_phone(phone)

    print("Contact added")

@args_num(2)
@input_error
def change_contact(*args):
    name, phone = args
    
    record = book[name]

    record.clear()
    record.add_phone(phone)

    print("Contact changed")


@args_num(1)
@input_error
def show_contact(name):
    record = book[name]
    print(record)


def show_all():
    if len(book) == 0:
        print("The address book is empty")
        return
    for record in book.values():
        print(record)

commands = {
    "hello": lambda: print("How can I help you?"),
    "add": add_contact,
    "change": change_contact,
    "phone": show_contact,
    "all": show_all,
}

def start():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command [hello,add,change,phone,all,exit]: ")
        command, args = parse_input(user_input)

        if command == "exit":
            print("Good bye!")
            break

        if command in commands:
            commands[command](*args)
        else:
            print("Invalid command")
