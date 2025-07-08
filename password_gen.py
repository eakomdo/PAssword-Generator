#A password generator

import random
import string
print("Hello! You are welcome to the password generator. Password length should be at least 8 charact.")

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return''.join(random.choice(characters) for _ in range(length))
  

def main():
   
    

    while True:
        try
        length = int(input("Enter the desired password length (minimum 8 characters): "))
        if length < 8:
            print("Password length should be at least 8 characters. Please try again.")
        else:
            break
    include_special_characters = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    if include_special_characters:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits

    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
