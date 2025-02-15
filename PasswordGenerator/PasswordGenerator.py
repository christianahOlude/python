import string
import random

def password_generator(length):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password = ""

    for count in range(0, length):
        password = password + random.choice(letters)


