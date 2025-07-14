# passd.py
from getpass import getpass

def main():
    password = getpass("Enter your password: ")
    print("Password entered successfully.")

if __name__ == "__main__":
    main()