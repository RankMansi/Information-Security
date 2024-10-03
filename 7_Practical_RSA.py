def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    t1, t2 = 0, 1
    r1, r2 = phi, e
    
    while r2 > 0:
        quotient = r1 // r2
        r1, r2 = r2, r1 - quotient * r2
        t1, t2 = t2, t1 - quotient * t2

    if r1 == 1:
        return t1 % phi

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))
e = int(input("Enter the public exponent e: "))
message = int(input("Enter the message to encrypt (as an integer): "))

n = p * q
phi = (p - 1) * (q - 1)

if gcd(e, phi) != 1:
    print("e and φ(n) are not co-prime. Please choose a different e.")
else:
    d = mod_inverse(e, phi)

    ciphertext = mod_exp(message, e, n)
    print(f"Encrypted message: {ciphertext}")

    decrypted_message = mod_exp(ciphertext, d, n)
    print(f"Decrypted message: {decrypted_message}")
