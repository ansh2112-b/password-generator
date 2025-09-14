import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    char_set = ''
    if use_letters:
        char_set += string.ascii_letters
    if use_numbers:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation

    if not char_set:
        print("Error: No character sets selected!")
        return None

    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def main():
    print("=== Random Password Generator ===")
    length = int(input("Enter password length: "))
    use_letters = input("Include letters? (yes/no): ").lower() == 'y'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'y'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
