# passd.py
# This script prompts the user to enter a password without echoing it to the console.
# It uses the getpass module to securely handle password input.
from getpass import getpass

def main():
    password = getpass("Enter your password: ")
    print("Password entered successfully.")

if __name__ == "__main__":
    main()