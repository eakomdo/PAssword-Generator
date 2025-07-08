#A password generator

import random
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return''.join(random.choice(characters) for _ in range(length))
  

def main():
    length = int(input("Enter the desired password length: "))
    include_special_characters = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    
    if include_special_characters:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits

    password = generate_password(length)
    print(f"Generated password: {password}")
    