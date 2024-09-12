def vigenere_encrypt(plaintext, keyword):
    def char_to_int(c):
        # Convert character to its corresponding alphabet index (0 for 'a', 25 for 'z')
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        return alphabet.index(c.lower())

    def int_to_char(i):
        # Convert alphabet index back to the character (0 -> 'a', 25 -> 'z')
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        return alphabet[i % 26]

    # Prepare the keyword
    keyword_length = len(keyword)
    keyword_as_int = [char_to_int(i) for i in keyword]

    # Encrypt the plaintext
    ciphertext = []
    keyword_index = 0

    for char in plaintext:
        if char.isalpha():  # Process only alphabetic characters
            shift = keyword_as_int[keyword_index % keyword_length]
            encrypted_char = int_to_char((char_to_int(char) + shift) % 26)
            ciphertext.append(encrypted_char)
            keyword_index += 1

    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, keyword):
    def char_to_int(c):
        # Convert character to its corresponding alphabet index (0 for 'a', 25 for 'z')
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        return alphabet.index(c.lower())

    def int_to_char(i):
        # Convert alphabet index back to the character (0 -> 'a', 25 -> 'z')
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        return alphabet[i % 26]

    # Prepare the keyword
    keyword_length = len(keyword)
    keyword_as_int = [char_to_int(i) for i in keyword]

    # Decrypt the ciphertext
    plaintext = []
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha():  # Process only alphabetic characters
            shift = keyword_as_int[keyword_index % keyword_length]
            decrypted_char = int_to_char((char_to_int(char) - shift + 26) % 26)
            plaintext.append(decrypted_char)
            keyword_index += 1

    return ''.join(plaintext)

# Get user input
plaintext = input("Enter the plaintext: ")
keyword = input("Enter the keyword: ")

# Encrypt the message
encrypted_message = vigenere_encrypt(plaintext, keyword)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = vigenere_decrypt(encrypted_message, keyword)
print("Decrypted message:", decrypted_message)
