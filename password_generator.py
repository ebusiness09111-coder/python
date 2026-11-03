import random
import string

def generate_password(length, use_digits=True, use_special=True):
    # Base characters are always lowercase and uppercase letters
    chars = string.ascii_letters
    
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    # Randomly select characters based on the specified length
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("--- Welcome to the Password Generator ---")
    try:
        user_length = int(input("Enter desired password length: "))
        include_digits = input("Include numbers? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        new_password = generate_password(user_length, include_digits, include_special)
        print(f"\nYour generated password is: {new_password}")
        print("----------------------------------------")
    except ValueError:
        print("Please enter a valid number for the length.")
