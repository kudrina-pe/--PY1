import string
from random import sample


def get_random_password(length) -> str:
    symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = "".join(sample(symbols, length))
    return password

print(get_random_password(8))
