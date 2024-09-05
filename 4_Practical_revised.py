def swap_pairs(message):
    swapped_message = []
    i = 0
    while i < len(message):
        if i + 1 < len(message):
            swapped_message.append(message[i + 1])
            swapped_message.append(message[i])
            i += 2
        else:
            swapped_message.append(message[i])
            i += 1
    return ''.join(swapped_message)

def fill_grid(message, key_length):
    num_rows = len(message) // key_length
    grid = ['' for _ in range(key_length)]
    
    for i in range(len(message)):
        grid[i % key_length] += message[i]
    
    return grid, num_rows

def print_grid(grid, num_rows):
    for row in range(num_rows):
        for col in range(len(grid)):
            if row < len(grid[col]):
                print(grid[col][row], end=' ')
            else:
                print(' ', end=' ')
        print()

def encrypt_columnar_cipher(message, key):
    key_length = len(key)
    
    # Swap pairs of letters
    swapped_message = swap_pairs(message)
    
    # Fill grid with swapped message
    grid, num_rows = fill_grid(swapped_message, key_length)
    
    print("Grid Formation:")
    print_grid(grid, num_rows)
    
    # Rearrange columns based on key
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    ciphertext = ''.join(grid[i] for i in key_order)

    return ciphertext

def decrypt_columnar_cipher(ciphertext, key):
    key_length = len(key)
    num_rows = len(ciphertext) // key_length
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    
    col_lengths = [len(ciphertext) // key_length] * key_length
    
    grid = ['' for _ in range(key_length)]
    index = 0
    for i in key_order:
        grid[i] = ciphertext[index:index + col_lengths[i]]
        index += col_lengths[i]
    
    # Reconstruct plaintext from grid
    plaintext = ''
    for i in range(num_rows):
        for col in grid:
            if i < len(col):
                plaintext += col[i]
    
    # Swap back pairs of letters
    def swap_back_pairs(message):
        original_message = []
        i = 0
        while i < len(message):
            if i + 1 < len(message):
                original_message.append(message[i + 1])
                original_message.append(message[i])
                i += 2
            else:
                original_message.append(message[i])
                i += 1
        return ''.join(original_message)
    
    return swap_back_pairs(plaintext)

# User input
message = input("Enter the message to encrypt: ")
key = input("Enter the key: ")

# Encryption
ciphertext = encrypt_columnar_cipher(message, key)
print("Encrypted message:", ciphertext)

# Decryption
decrypted_message = decrypt_columnar_cipher(ciphertext, key)
print("Decrypted message:", decrypted_message)
