# Mapping letters to numbers and vice versa
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTER_TO_NUM = {char: i for i, char in enumerate(LETTERS)}
NUM_TO_LETTER = LETTERS

def text_to_numbers(text):
    return [LETTER_TO_NUM[char.upper()] for char in text]

def numbers_to_text(numbers):
    return ''.join(NUM_TO_LETTER[num % 26] for num in numbers)

def hill_cipher_block_encrypt(a, b, key_matrix):
    x = (key_matrix[0][0] * a + key_matrix[0][1] * b) % 26
    y = (key_matrix[1][0] * a + key_matrix[1][1] * b) % 26
    return x, y

def hill_cipher_block_decrypt(a, b, inv_key_matrix):
    x = (inv_key_matrix[0][0] * a + inv_key_matrix[0][1] * b) % 26
    y = (inv_key_matrix[1][0] * a + inv_key_matrix[1][1] * b) % 26
    return x, y

def mod_inverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse exists for {a} under mod {m}")

def inverse_matrix_2x2(matrix):
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
    det_inv = mod_inverse(det)
    return [
        [matrix[1][1] * det_inv % 26, -matrix[0][1] * det_inv % 26],
        [-matrix[1][0] * det_inv % 26, matrix[0][0] * det_inv % 26]
    ]

def hill_cipher_encrypt(plaintext, key_matrix):    
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a = LETTER_TO_NUM[plaintext[i].upper()]
        b = LETTER_TO_NUM[plaintext[i + 1].upper()]
        x, y = hill_cipher_block_encrypt(a, b, key_matrix)
        ciphertext += NUM_TO_LETTER[x] + NUM_TO_LETTER[y]
    
    return ciphertext
def hill_cipher_decrypt(ciphertext, key_matrix):
    inv_key_matrix = inverse_matrix_2x2(key_matrix)
    
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a = LETTER_TO_NUM[ciphertext[i].upper()]
        b = LETTER_TO_NUM[ciphertext[i + 1].upper()]
        x, y = hill_cipher_block_decrypt(a, b, inv_key_matrix)
        plaintext += NUM_TO_LETTER[x] + NUM_TO_LETTER[y]
    
    return plaintext

plaintext = input("Enter the plaintext: ").upper()

print("Enter the 2x2 key matrix (4 integers):")
key_matrix = [
    list(map(int, input("Enter row 1 (2 space-separated integers): ").split())),
    list(map(int, input("Enter row 2 (2 space-separated integers): ").split()))
]

ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
print(f"Ciphertext: {ciphertext}")

decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)
print(f"Decrypted Text: {decrypted_text}")
