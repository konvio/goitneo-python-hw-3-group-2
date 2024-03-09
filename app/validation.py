def validate_phone(value: str):
    if len(value) != 10 or not value.isdigit():
        raise ValueError("Phone number must be 10 digits long")


def input_error(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ValueError as e:
            print(f"Input error: {str(e)}")
        except KeyError as e:
            print(f"Contact not found: {str(e)}")
    return wrapper


def args_num(num: int):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if len(args) != num:
                print(f"Invalid number of arguments. Expected {num}, got {len(args)}")
                return
            return function(*args, **kwargs)
        return wrapper
    return decorator
