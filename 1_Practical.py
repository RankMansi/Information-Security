def clean_text(text):
    return ''.join(char for char in text if char.isalpha())

def encrypt_caesar_cipher(text, key=17):
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    
    cleaned_text = clean_text(text)

    for char in cleaned_text:
        if char in alphabet_upper:
            P = alphabet_upper.index(char)
            C = (P + key) % 26
            result += alphabet_upper[C]
        elif char in alphabet_lower:
            P = alphabet_lower.index(char)
            C = (P + key) % 26
            result += alphabet_lower[C]

    return result

def decrypt_caesar_cipher(text, key=17, original_text=""):
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    index = 0

    for char in original_text:
        if char in alphabet_upper:
            C = alphabet_upper.index(text[index])
            P = (C - key) % 26
            result += alphabet_upper[P]
            index += 1
        elif char in alphabet_lower:
            C = alphabet_lower.index(text[index])
            P = (C - key) % 26
            result += alphabet_lower[P]
            index += 1
        else:
            result += char  # Preserve spaces

    return result

# Get user input
plaintext = input("Enter the text to be encrypted: ")

# Encrypt the text
encrypted_text = encrypt_caesar_cipher(plaintext)
print(f"Encrypted Text: {encrypted_text}")

# Decrypt the text
decrypted_text = decrypt_caesar_cipher(encrypted_text, 17, plaintext)
print(f"Decrypted Text: {decrypted_text}")
