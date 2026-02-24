import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password

# Ask user for password length
n = int(input("Enter password length: "))
print("Generated Password:", generate_password(n))

# Help from Ai