from re import M
from MR import isProbablyPrime, quickModularExponent
from math import gcd
import random

'''
    Global variables for key size
'''
min = 2**32
max = 2**64-1

'''
    Generates a prime number. Uses Miller-Rabin as primality test.
    Parameters :
        - a minimal power of 2 min
        - a maximal power of 2 max
'''


def generate_prime():
    r = random.randint(min, max)
    while(not isProbablyPrime(r)):
        r = random.randint(min, max)
    return r


'''
    Finds a number coprime with phi
    Parameters :
        - The value phi = (p-1) * (q-1)

    Returns :
        A number e such as 1 < e < phi(n) and gcd(e,phi(n)) = 1

'''


def find_coprime(phi):
    for i in range(2, phi):
        if (gcd(i, phi) == 1):
            return i
    return -1


'''
    Find the phi modular inverse of e using Euclide's algorithm
    Parameters :
        - The number e
        - The modulo phi
    Returns
        A number d such as ed = 1 mod phi
'''


def find_inverse(e, phi):
    m = phi
    x = 1
    y = 0

    if(phi == 1):
        return 0
    while (e > 1):
        q = e//phi
        t = phi

        phi, e, t = e % phi, t, y
        y, x = x-q*t, t

    if (x < 0):
        x += m
    return x


'''
    Generates public and private keys for RSA
    Parameters :
        None

    Returns :
        A list [(n,e),(d,n)] containing the public and the private keys
'''


def generate_RSA():
    p, q = generate_prime(), generate_prime()
    if (q == p):
        q = generate_prime()

    n = p*q
    phi = (p-1) * (q-1)
    e = find_coprime(phi)

    d = find_inverse(e, phi)
    return [[n, e], [d, n]]


'''
    Encrypts a message using RSA
    Parameters :
        - msg : the message to encrypt
        - key : the public key (n,e)

    Returns :
        The encrypted message
'''


def encrypt_RSA(msg, key):
    binary = bin(msg[0])
    for i in range(1, len(msg)):
        binary += bin(msg[i])[2::]

    binary = bin(quickModularExponent(int(binary, base=2), key[1], key[0]))

    cyphered = ""
    for i in range(2, len(binary), 8):
        cyphered += chr(int(binary[i:i+7], base=2))
    return cyphered


'''
    Decrypt a message using RSA
    Parameters :
        - msg : the message to decrypt
        - key : the private key (d,n)

    Returns :
        The raw message
'''


def decrypt_RSA(msg, key):
    binary = bin(msg[0])
    for i in range(1, len(msg)):
        binary += bin(msg[i])[2::]

    binary = bin(quickModularExponent(int(binary, base=2), key[0], key[1]))

    raw = ""
    for i in range(2, len(binary), 8):
        raw += chr(int(binary[i:i+7], base=2))
    return raw


'''
    TESTS
'''


def main():
    print("Generated keys : ")
    k = generate_RSA()
    print(k)

    print("Encrypt 'HELLO' :")
    m = encrypt_RSA("HELLO", k[0])
    print(m)

    print("Decrypt 'HELLO' : ")
    print(decrypt_RSA(m, k[1]))


if __name__ == "__main__":
    main()
