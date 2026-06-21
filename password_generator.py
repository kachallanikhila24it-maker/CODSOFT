import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters

if input("Include numbers? (y/n): ").lower() == 'y':
    characters += string.digits

if input("Include symbols? (y/n): ").lower() == 'y':
    characters += string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:", password)
