def encrypt_rail_fence(text, key):
    rails = [''] * key
    row = 0
    direction = 1

    # Initialize an empty list of strings for each rail
    pattern = [[' ' for _ in range(len(text))] for _ in range(key)]

    for col, char in enumerate(text):
        rails[row] += char
        pattern[row][col] = char  # Place the character in the pattern grid
        
        row += direction

        if row == 0 or row == key - 1:
            direction *= -1

    # Print the horizontal pattern
    print("Pattern Formation:")
    for r in pattern:
        print("".join(r))  # Join the characters with no space in between

    return ''.join(rails)


# def encrypt_rail_fence(text, key):
#     # Create a list of empty strings for each row
#     rails = [''] * key
#     row = 0
#     direction = 1  # 1 for down, -1 for up

#     for char in text:
#         # Add the character to the current row
#         rails[row] += char
#         # Move to the next row
#         row += direction
        
#         # Change direction if we hit the top or bottom row
#         if row == 0 or row == key - 1:
#             direction *= -1
    
#     # Combine all rows to form the encrypted text
#     return ''.join(rails)


def decrypt_rail_fence(cipher, key):
    rails = [''] * key
    position = [0] * len(cipher)
    row = 0
    direction = 1

    for i in range(len(cipher)):
        position[i] = row
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1

    index = 0
    for r in range(key):
        for i in range(len(cipher)):
            if position[i] == r:
                rails[r] += cipher[index]
                index += 1

    result = ''
    row = 0
    direction = 1
    for i in range(len(cipher)):
        result += rails[row][0]
        rails[row] = rails[row][1:]
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1

    return result

text = input("Enter the text to encrypt: ")
key = int(input("Enter the key (number of rails): "))

encrypted = encrypt_rail_fence(text, key)
decrypted = decrypt_rail_fence(encrypted, key)

print("\nOriginal Text: " + text)
print("Encrypted Text: " + encrypted)
print("Decrypted Text: " + decrypted)