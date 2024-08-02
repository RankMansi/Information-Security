def clean_text(text):
    cleaned = ""
    for char in text:
        if char.isalpha():
            cleaned += char
    return cleaned

def generate_key_from_passphrase(passphrase, length):
    key = ""
    for i in range(length):
        key += passphrase[i % len(passphrase)]
    return key

# Manually created lists of uppercase and lowercase alphabets
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def char_to_index(char, alphabet):
    for i in range(len(alphabet)):
        if alphabet[i] == char:
            return i
    return -1

def index_to_char(index, alphabet):
    return alphabet[index]

def encrypt_caesar_cipher(text, passphrase):
    result = ""
    cleaned_text = clean_text(text)
    
    key = generate_key_from_passphrase(passphrase, len(cleaned_text))
    dynamic_keys = [char_to_index(char, alphabet_lower) % 26 for char in key]  # Assuming passphrase is lowercase
    
    for index in range(len(cleaned_text)):
        char = cleaned_text[index]
        dynamic_key = dynamic_keys[index]
        if char in alphabet_upper:
            P = char_to_index(char, alphabet_upper)
            C = (P + dynamic_key) % 26
            result += index_to_char(C, alphabet_upper)
        elif char in alphabet_lower:
            P = char_to_index(char, alphabet_lower)
            C = (P + dynamic_key) % 26
            result += index_to_char(C, alphabet_lower)

    return result

def decrypt_caesar_cipher(text, passphrase, original_text):
    result = ""
    cleaned_text = clean_text(original_text)
    
    key = generate_key_from_passphrase(passphrase, len(cleaned_text))
    dynamic_keys = [char_to_index(char, alphabet_lower) % 26 for char in key]  # Assuming passphrase is lowercase
    
    for index in range(len(cleaned_text)):
        char = cleaned_text[index]
        dynamic_key = dynamic_keys[index]
        if char in alphabet_upper:
            C = char_to_index(text[index], alphabet_upper)
            P = (C - dynamic_key) % 26
            result += index_to_char(P, alphabet_upper)
        elif char in alphabet_lower:
            C = char_to_index(text[index], alphabet_lower)
            P = (C - dynamic_key) % 26
            result += index_to_char(P, alphabet_lower)
        else:
            result += char  # Preserve spaces

    return result

# Get user input
plaintext = input("Enter the text to be encrypted: ")
passphrase = input("Enter the passphrase: ")

# Encrypt the text
encrypted_text = encrypt_caesar_cipher(plaintext, passphrase)
print(f"Encrypted Text: {encrypted_text}")

# Decrypt the text
decrypted_text = decrypt_caesar_cipher(encrypted_text, passphrase, plaintext)
print(f"Decrypted Text: {decrypted_text}")
