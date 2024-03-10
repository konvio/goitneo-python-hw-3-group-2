def validate_phone(value: str):
    if len(value) != 10 or not value.isdigit():
        raise ValueError("Phone number must be 10 digits long")



