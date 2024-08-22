def generate_key_table(key):
    key = key.replace('j', 'i')  
    seen = set()
    key_table = [char for char in key if char not in seen and not seen.add(char)]
    key_table += [char for char in "abcdefghiklmnopqrstuvwxyz" if char not in key_table]
    return [key_table[i:i+5] for i in range(0, 25, 5)]

def format_text(text):
    text = ''.join(filter(str.isalpha, text)).replace("j", "i")  
    formatted_text = ""
    i = 0
    while i < len(text):
        formatted_text += text[i]
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                formatted_text += 'x'
            else:
                formatted_text += text[i + 1]
                i += 1
        i += 1
    return formatted_text + ('x' if len(formatted_text) % 2 != 0 else '')

def find_position(char, key_matrix):
    for i, row in enumerate(key_matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair_encrypt(text, key):
    key_matrix = generate_key_table(key)
    formatted_text = format_text(text)
    cipher_text = ""
    for i in range(0, len(formatted_text), 2):
        row1, col1 = find_position(formatted_text[i], key_matrix)
        row2, col2 = find_position(formatted_text[i + 1], key_matrix)
        if row1 == row2:
            cipher_text += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            cipher_text += key_matrix[row1][col2] + key_matrix[row2][col1]
    return cipher_text

def playfair_decrypt(cipher_text, key):
    key_matrix = generate_key_table(key)
    decrypted_text = ""
    for i in range(0, len(cipher_text), 2):
        row1, col1 = find_position(cipher_text[i], key_matrix)
        row2, col2 = find_position(cipher_text[i + 1], key_matrix)
        if row1 == row2:
            decrypted_text += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]
    
    # Clean up filler 'x'
    cleaned_text = ""
    skip_next = False
    for i in range(len(decrypted_text)):
        if skip_next:
            skip_next = False
            continue
        if decrypted_text[i] == 'x' and (i == len(decrypted_text) - 1 or decrypted_text[i-1] == decrypted_text[i+1]):
            continue
        cleaned_text += decrypted_text[i]
        if i < len(decrypted_text) - 1 and decrypted_text[i] == decrypted_text[i+1]:
            skip_next = True

    return cleaned_text

def print_key_matrix(key_matrix):
    print("Key Matrix:")
    for row in key_matrix:
        print(" ".join(row))


key = input("Enter the key for encryption: ")
plaintext = input("Enter the plaintext to encrypt: ")

key_matrix = generate_key_table(key)
print_key_matrix(key_matrix)
cipher_text = playfair_encrypt(plaintext, key)
decrypted_text = playfair_decrypt(cipher_text, key)

print(f"\nPlaintext: {plaintext}")
print(f"Ciphertext: {cipher_text}")
print(f"Decrypted Text: {decrypted_text}")