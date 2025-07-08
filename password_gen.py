#A password generator

import random
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
   