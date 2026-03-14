import random
import string

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    all_characters = letters + digits + symbols

    # ensure strong password
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_characters, k=length-4)

    random.shuffle(password)

    return "".join(password)


print("----- Strong Password Generator -----")

while True:
    password = generate_password()
    print("Generated Password:", password)

    choice = input("Do you like this password? (yes/no): ").lower()

    if choice == "yes":
        print("Your final password is:", password)
        break
    else:
        print("Generating a new password...\n")
