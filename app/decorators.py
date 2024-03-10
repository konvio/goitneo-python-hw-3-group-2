import functools


def handle_errors(function):

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ValueError as e:
            print(f"Invalid value: {str(e)}")
        except KeyError as e:
            print(f"Not found: {str(e)}")

    return wrapper


def args_len(num: int):
    def decorator(function):

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            if len(args) != num:
                print(f"Invalid number of arguments. Expected {num}, got {len(args)}")
                return
            return function(*args, **kwargs)

        return wrapper

    return decorator
