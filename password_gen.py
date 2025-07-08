#A password generator

import random
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return''.join(random.choice(characters) for _ in range(length))
  

  if include_special_characters == True:
    characters += string.punctuation
    