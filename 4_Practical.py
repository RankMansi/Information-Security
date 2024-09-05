def print_grid(grid, num_rows):
    for row in range(num_rows):
        row_str = " ".join(grid[col][row] if row < len(grid[col]) else " " for col in range(len(grid)))
        print(row_str)
    print()

def encrypt_columnar_cipher(message, key):
    message = message.replace(" ", "")
    num_rows = len(message) // len(key) + (len(message) % len(key) != 0)
    grid = ['' for _ in range(len(key))]

    for idx, char in enumerate(message):
        grid[idx % len(key)] += char

    print("Grid Formation:")
    print_grid(grid, num_rows)

    key_order = sorted(range(len(key)), key=lambda k: key[k])
    ciphertext = ''.join(grid[i] for i in key_order)
    
    return ciphertext

def decrypt_columnar_cipher(ciphertext, key):
    num_rows = len(ciphertext) // len(key) + (len(ciphertext) % len(key) != 0)
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    col_lengths = [len(ciphertext) // len(key)] * len(key)
    
    for i in range(len(ciphertext) % len(key)):
        col_lengths[key_order[i]] += 1

    grid = ['' for _ in range(len(key))]
    index = 0
    for i in key_order:
        grid[i] = ciphertext[index:index + col_lengths[i]]
        index += col_lengths[i]

    plaintext = ''
    for i in range(num_rows):
        for col in grid:
            if i < len(col):
                plaintext += col[i]

    return plaintext

# User input
message = input("Enter the message to encrypt: ")
key = input("Enter the key: ")

# Encryption
ciphertext = encrypt_columnar_cipher(message, key)
print("Encrypted message:", ciphertext)

# Decryption
decrypted_message = decrypt_columnar_cipher(ciphertext, key)
print("Decrypted message:", decrypted_message)