import re
import random
import string
import maskpass
import os
import hashlib

emailtest = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def isValid(email):
    if re.fullmatch(emailtest, email):
        return True
    else:
        return False


import re  # Import the 're' module for regular expressions

def isValidpass(password):
    """
    Validates a password based on certain criteria.

    Parameters:
    password (str): The password to be validated.

    Returns:
    int: 1 if the password is valid, 0 if it's not.
    """

    # Initialize counters for lowercase letters, uppercase letters, digits, and symbols.
    lower_count = 0
    upper_count = 0
    digit_count = 0
    symbol_count = 0

    # Check if the password length is at least 8 characters.
    if len(password) >= 8:
        # Iterate through each character in the password.
        for char in password:
            if char.islower():
                lower_count += 1  # Increment lowercase letter count.
            if char.isupper():
                upper_count += 1  # Increment uppercase letter count.
            if char.isdigit():
                digit_count += 1  # Increment digit count.
            if re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\]', char):
                symbol_count += 1  # Increment symbol count.
    else:
        print("Please enter a password of at least 8 characters.")
        return 0

    # Check and display messages for missing character types.
    if lower_count == 0:
        print("Please use at least one lowercase character.")
    if upper_count == 0:
        print("Please use at least one uppercase character.")
    if digit_count == 0:
        print("Please use at least one digit.")
    if symbol_count == 0:
        print("Please use at least one symbol.")

    # If all criteria are met, the password is valid.
    if lower_count != 0 and upper_count != 0 and digit_count != 0 and symbol_count != 0:
        return 1
    return 0

# Example usage:
result = isValidpass("P@ssw0rd")
print("Password is valid" if result == 1 else "Password is not valid")


def generate_password():
    """
    Generates a random password that meets specific criteria.

    Returns:
    str: A randomly generated password.
    """

    while True:
        test = '1'
        pwd = ""
        x = random.randint(6, 8)  # Random password length between 6 and 8 characters.

        # Generate a password with the specified length.
        for i in range(x):
            p = random.randint(1, 4)
            if p == 1:
                pwd += random.choice(string.ascii_lowercase)  # Add a lowercase letter.
            elif p == 2:
                pwd += random.choice(string.ascii_uppercase)  # Add an uppercase letter.
            elif p == 3:
                pwd += random.choice(string.digits)  # Add a digit.
            elif p == 4:
                pwd += random.choice(string.punctuation)  # Add a symbol.

        # Initialize counters for lowercase letters, uppercase letters, digits, and symbols.
        lower_count = 0
        upper_count = 0
        digit_count = 0
        symbol_count = 0

        # Count the character types in the generated password.
        for char in pwd:
            if char.islower():
                lower_count += 1
            if char.isupper():
                upper_count += 1
            if char.isdigit():
                digit_count += 1
            if not char.isalnum():
                symbol_count += 1

        # Check if the generated password meets the criteria.
        if lower_count != 0 and upper_count != 0 and digit_count != 0 and symbol_count != 0:
            test = '0'

        # If the criteria are met, return the generated password.
        if test == '0':
            return pwd


# Example usage:
random_password = generate_password()
print("Random Password:", random_password)


def ciphercaesar(text, shift):
    """
    Encrypts a message using the Caesar cipher.

    Args:
    text (str): The input text to be encrypted.
    shift (int): The number of positions to shift the letters.

    Returns:
    str: The encrypted message.
    """
    # Define the alphabet for reference.
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Initialize the result as an empty string.
    result = ''

    # Convert the input text to uppercase to work with a consistent case.
    text = text.upper()

    # Iterate through each character in the input text.
    for char in text:
        if char.isalpha():  # Check if the character is a letter.
            # Find the index of the character in the alphabet and apply the shift.
            shifted_index = (alphabet.index(char) + int(shift)) % 26  # Cast shift to int

            # Append the shifted character to the result.
            result += alphabet[shifted_index]
        else:
            # If the character is not a letter, keep it unchanged.
            result += char

    return result

# Example usage:
plaintext = "HELLO"
shift_amount = 3
encrypted_text = ciphercaesar(plaintext, shift_amount)
print("Encrypted Text:", encrypted_text)



def ciphercaesar2(text, shift):
    """
    Decrypts a message encrypted with the Caesar cipher.

    Args:
    text (str): The input text to be decrypted.
    shift (int): The number of positions to shift the letters for decryption.

    Returns:
    str: The decrypted message.
    """
    # Define the alphabet for reference.
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Initialize the result as an empty string.
    result = ''

    # Convert the input text to uppercase to work with a consistent case.
    text = text.upper()

    # Iterate through each character in the input text.
    for char in text:
        if char.isalpha():  # Check if the character is a letter.
            # Find the index of the character in the alphabet and apply the reverse shift for decryption.
            shifted_index = (alphabet.index(char) - int(shift)) % 26

            # Append the shifted character to the result.
            result += alphabet[shifted_index]
        else:
            # If the character is not a letter, keep it unchanged.
            result += char

    return result


# Example usage:
encrypted_text = "KHOOR"
shift_amount = 3
decrypted_text = ciphercaesar2(encrypted_text, shift_amount)
print("Decrypted Text:", decrypted_text)


def ciphercaesarASCII(text, shift):
    """
    Encrypts a message using the Caesar cipher with ASCII characters.

    Args:
    text (str): The input text to be encrypted.
    shift (int): The number of positions to shift the characters for encryption.

    Returns:
    str: The encrypted message.
    """
    # Initialize an empty string for the result.
    result = ''

    # Convert the input text to uppercase to work with a consistent case.
    text = text.upper()

    # Iterate through each character in the input text.
    for char in text:
        if char.isalpha():  # Check if the character is a letter.
            # Apply the Caesar cipher to letters by converting ASCII values.
            encrypted_char = chr((ord(char) + int(shift) - ord('A')) % 26 + ord('A'))

            # Append the encrypted character to the result.
            result += encrypted_char
        else:
            # If the character is not a letter, keep it unchanged.
            result += char

    return result


# Example usage:
plain_text = "HELLO"
shift_amount = 3
encrypted_text = ciphercaesarASCII(plain_text, shift_amount)
print("Encrypted Text:", encrypted_text)


def ciphercaesarASCII2(text, shift):
    """
    Decrypts a message encrypted using the Caesar cipher with ASCII characters.

    Args:
    text (str): The encrypted text to be decrypted.
    shift (int): The number of positions the characters were shifted during encryption.

    Returns:
    str: The decrypted message.
    """
    # Initialize an empty string for the result.
    result = ''

    # Convert the input text to uppercase to work with a consistent case.
    text = text.upper()

    # Iterate through each character in the input text.
    for char in text:
        if char.isalpha():  # Check if the character is a letter.
            # Apply the reverse Caesar cipher to letters by converting ASCII values.
            decrypted_char = chr((ord(char) - int(shift) - ord('A')) % 26 + ord('A'))

            # Append the decrypted character to the result.
            result += decrypted_char
        else:
            # If the character is not a letter, keep it unchanged.
            result += char

    return result


# Example usage:
encrypted_text = "KHOOR"
shift_amount = 3
decrypted_text = ciphercaesarASCII2(encrypted_text, shift_amount)
print("Decrypted Text:", decrypted_text)
