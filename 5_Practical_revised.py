# Function to modify the key by splitting it into two halves, adjusting the first half for odd lengths, and reversing the second half
def modify_key(key):
    key_len = len(key)
    
    # Calculate the split index
    if key_len % 2 == 0:
        half_len = key_len // 2
    else:
        half_len = (key_len + 1) // 2 - 1
    
    # First half stays the same
    first_half = key[:half_len]
    
    # Second half is reversed
    second_half = key[half_len:][::-1]
    
    # Return the modified key
    return first_half + second_half

# Function to encrypt the plaintext using the modified key
def encrypt(plaintext, key):
    key = modify_key(key)
    ciphertext = []
    
    for i in range(len(plaintext)):
        if 'a' <= plaintext[i] <= 'z':  # Encrypt only lowercase letters
            # Shifting characters manually
            shift = (ord(plaintext[i]) - ord('a') + ord(key[i % len(key)]) - ord('a')) % 26
            ciphertext.append(chr(shift + ord('a')))
        else:
            ciphertext.append(plaintext[i])  # Non-alphabet characters remain unchanged
    
    return ''.join(ciphertext)

# Function to decrypt the ciphertext using the modified key
def decrypt(ciphertext, key):
    key = modify_key(key)
    decrypted_text = []
    
    for i in range(len(ciphertext)):
        if 'a' <= ciphertext[i] <= 'z':  # Decrypt only lowercase letters
            # Reversing the shift manually
            shift = (ord(ciphertext[i]) - ord('a') - (ord(key[i % len(key)]) - ord('a')) + 26) % 26
            decrypted_text.append(chr(shift + ord('a')))
        else:
            decrypted_text.append(ciphertext[i])  # Non-alphabet characters remain unchanged
    
    return ''.join(decrypted_text)

# Main function to run the program
def main():
    plaintext = input("Enter the plaintext (only lowercase letters): ").strip()
    key = input("Enter the key (only lowercase letters): ").strip()

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext:    ", ciphertext)

    # Decrypt the ciphertext
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
