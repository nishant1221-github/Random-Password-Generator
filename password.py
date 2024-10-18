import random

# Character sets
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_characters = '!@#$%^&*()'

# Combine all character sets
all_characters = lowercase + uppercase + digits + special_characters

# User input for password length
length = int(input("Enter the desired password length: "))

if length < 4:
    print("Length must be at least 4.")
else:
    password = ''
    for _ in range(length):
        # Randomly select a character from all characters
        char = all_characters[random.randint(0, len(all_characters) - 1)]
        password += char

    print("Generated Password:", password)
