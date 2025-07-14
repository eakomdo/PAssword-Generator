# passd.py
# This script prompts the user to enter a password without echoing it to the console.
# It uses the getpass module to securely handle password input.
# It is useful for scenarios where sensitive information needs to be entered without being visible on the screen.
# The code is designed to be user-friendly and provides clear instructions for input.
# The password is stored securely in memory and not displayed on the console.
# The code is compatible with Python 3 and can be run in any Python environment.
# The password input process is secure and follows best practices for handling sensitive information.
from getpass import getpass

def main():
    password = getpass("Enter your password: ")
    print("Password entered successfully.")

if __name__ == "__main__":
    main()