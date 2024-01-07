import string
import random

def generate_password(length, min_letters=0, min_digits=0):
    if(min_letters + min_digits > length):
        raise ValueError("Nieprawidłowa złożoność hasła")
    password=""
    letters=0
    digits=0
    generator = character_generator()
    while len(password) < length:
        character = next(generator)
        digits_left = min_digits - digits
        letters_left = min_letters - letters
        chars_left = length - len(password)
        if(character.isalpha()):
            if(digits_left == chars_left):
                continue
            letters += 1
        if(character.isdigit()):
            if(letters_left == chars_left):
                continue
            digits += 1
        password += character
    return password

def character_generator():
    while True:
        yield random.choice(string.ascii_letters + string.digits)

def password_generator(limit, length, min_letters=0, min_digits=0):
    for i in range(limit):
        yield generate_password(length, min_letters, min_digits)

for password in password_generator(5, 12, 4, 4):
    print(password)
