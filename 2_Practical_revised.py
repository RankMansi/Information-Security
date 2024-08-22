def generate_key_table(key):
    key = key.replace('j', 'i')
    seen = {}
    key_table = []
    for char in key:
        if char not in seen:
            seen[char] = True
            key_table.append(char)
    
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in seen:
            key_table.append(char)
    
    # Complex pattern for shuffling
    pattern = [1, 4, 0, 3, 2]
    shuffled_table = []
    for i in range(0, 25, 5):
        row = [key_table[i + pattern[j]] for j in range(5)]
        shuffled_table.extend(row)
    
    key_matrix = [shuffled_table[i:i+5] for i in range(0, 25, 5)]
    
    return key_matrix

def print_key_matrix(key_matrix):
    print("Key Matrix:")
    for row in key_matrix:
        print(" ".join(row))

def format_text(text):
    text = text.replace('j', 'i')
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
    for i in range(5):
        if char in key_matrix[i]:
            return i, key_matrix[i].index(char)
    return None

def playfair_encrypt(text, key_matrix):
    formatted_text = format_text(text)
    cipher_text = ""
    
    for i in range(0, len(formatted_text), 2):
        char1 = formatted_text[i]
        char2 = formatted_text[i + 1]
        
        pos1 = find_position(char1, key_matrix)
        pos2 = find_position(char2, key_matrix)
        
        if pos1 is None or pos2 is None:
            raise ValueError(f"Character not found in key matrix: {char1 if pos1 is None else char2}")
        
        row1, col1 = pos1
        row2, col2 = pos2
        
        if row1 == row2:
            cipher_text += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            cipher_text += key_matrix[row1][col2] + key_matrix[row2][col1]
    
    return cipher_text

def playfair_decrypt(cipher_text, key_matrix):
    decrypted_text = ""
    
    for i in range(0, len(cipher_text), 2):
        char1 = cipher_text[i]
        char2 = cipher_text[i + 1]
        
        pos1 = find_position(char1, key_matrix)
        pos2 = find_position(char2, key_matrix)
        
        if pos1 is None or pos2 is None:
            raise ValueError(f"Character not found in key matrix: {char1 if pos1 is None else char2}")
        
        row1, col1 = pos1
        row2, col2 = pos2
        
        if row1 == row2:
            decrypted_text += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]

    return decrypted_text

key = input("Enter the key for encryption: ")
plaintext = input("Enter the plaintext to encrypt: ")

key_matrix = generate_key_table(key)
print_key_matrix(key_matrix)  # Print key matrix only once

cipher_text = playfair_encrypt(plaintext, key_matrix)
decrypted_text = playfair_decrypt(cipher_text, key_matrix)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {cipher_text}")
print(f"Decrypted Text: {decrypted_text}")
