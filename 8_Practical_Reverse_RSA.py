import math
import random

def generate_prime_numbers(bits):
    """Generates two prime numbers of specified bit length."""
    while True:
        p = random.getrandbits(bits) | 1  # Ensure p is odd
        if is_prime(p):
            break
    while True:
        q = random.getrandbits(bits) | 1  # Ensure q is odd
        if is_prime(q) and p != q:
            break
    return p, q

def is_prime(num):
    """Checks if a number is prime using the Miller-Rabin test."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    r, d = num - 1, 0
    while r % 2 == 0:
        r //= 2
        d += 1
    for _ in range(10):  # Adjust the number of iterations for desired accuracy
        a = random.randint(2, num - 2)
        x = pow(a, r, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(d - 1):
            x = (x * x) % num
            if x == num - 1:
                break
        else:
            return False
    return True

def extended_gcd(a, b):
    """Return gcd(a, b), and x, y such that a * x + b * y = gcd(a, b)."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(e, phi):
    """Computes the modular inverse of e mod phi."""
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Inverse doesn't exist")
    return x % phi

def generate_keys(p, q):
    """Generates public and private keys."""
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random.randint(2, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    d = modular_inverse(e, phi_n)
    return (n, e), (n, d)

def encrypt(message, public_key):
    """Encrypts a message using the public key."""
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]  # Encrypt each character
    return encrypted_message

def decrypt(encrypted_message, private_key):
    """Decrypts a message using the private key."""
    n, d = private_key
    decrypted_message = ''.join(chr(pow(char, d, n)) for char in encrypted_message)  # Decrypt each character
    return decrypted_message

def sign_message(message, private_key):
    """Signs a message using the private key."""
    return encrypt(message, private_key)

def verify_signature(message, signature, public_key):
    """Verifies a signature using the public key."""
    decrypted_message = decrypt(signature, public_key)
    return message == decrypted_message

# Example usage:
if __name__ == "__main__":
    bits = 16  # Change this to a larger number for actual use (e.g., 1024)
    p, q = generate_prime_numbers(bits)
    public_key, private_key = generate_keys(p, q)

    # Take user input for the message
    message = input("Enter a message to sign: ")
    signature = sign_message(message, private_key)

    if verify_signature(message, signature, public_key):
        print("Signature verified!")
    else:
        print("Signature invalid!")

    # Output the signature and decrypted message for verification
    print("Signature:", signature)
    decrypted_message = decrypt(signature, public_key)
    print("Decrypted message:", decrypted_message)
