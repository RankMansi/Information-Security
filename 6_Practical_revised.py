import random
def determinant(matrix):
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26

def shuffle_key_matrix(key_matrix):
    for i in range(2):
        random.shuffle(key_matrix[i])  
    random.shuffle(key_matrix)
    return key_matrix

def matrix_multiply(block, key_matrix):
    return [(block[0] * key_matrix[0][0] + block[1] * key_matrix[1][0]) % 26,
            (block[0] * key_matrix[0][1] + block[1] * key_matrix[1][1]) % 26]

def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def inverse_matrix_2x2(matrix):
    det_inv = mod_inverse(determinant(matrix), 26)
    if det_inv is None:
        raise ValueError("The matrix is not invertible.")
    
    return [[(matrix[1][1] * det_inv) % 26, (-matrix[0][1] * det_inv) % 26],
            [(-matrix[1][0] * det_inv) % 26, (matrix[0][0] * det_inv) % 26]]

def hill_cipher_encrypt(plaintext, key_matrix):
    return ''.join(numbers_to_text(matrix_multiply(text_to_numbers(plaintext[i:i + 2]), key_matrix))
                   for i in range(0, len(plaintext), 2))

def hill_cipher_decrypt(ciphertext, key_matrix):
    inv_key_matrix = inverse_matrix_2x2(key_matrix)
    return ''.join(numbers_to_text(matrix_multiply(text_to_numbers(ciphertext[i:i + 2]), inv_key_matrix))
                   for i in range(0, len(ciphertext), 2))

key_matrix = [list(map(int, input(f"Enter row {i + 1} (2 space-separated integers): ").split())) for i in range(2)]
shuffled_key_matrix = shuffle_key_matrix(key_matrix)

print("\nShuffled Key Matrix (after swapping rows and shuffling elements):")
for row in shuffled_key_matrix:
    print(row)

plaintext = input("\nEnter the 4-letter plaintext: ").upper()
if len(plaintext) != 4:
    raise ValueError("Plaintext must be exactly 4 letters.")

ciphertext = hill_cipher_encrypt(plaintext, shuffled_key_matrix)
print(f"\nCiphertext: {ciphertext}")

decrypted_text = hill_cipher_decrypt(ciphertext, shuffled_key_matrix)
print(f"Decrypted Text: {decrypted_text}")
