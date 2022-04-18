from re import M
from MR import isProbablyPrime,quickExponent
from math import gcd
import random

'''
    Generates a prime number. Uses Miller-Rabin as primality test.
    Parameters :
        - a minimal power of 2 min
        - a maximal power of 2 max
'''
def generate_prime(min,max):
    if (min > max) : 
        min,max = max,min
    elif min == max :
        max = min+1

    r = random.randint(2**min, 2**max)
    while(not isProbablyPrime(r)) :
        r = random.randint(2**64,2**128)
    return r

'''
    Finds a number coprime with phi
    Parameters :
        - The value phi = (p-1) * (q-1)

    Returns :
        A number e such as 1 < e < phi(n) and gcd(e,phi(n)) = 1

'''
def find_coprime(phi):
    for i in range (2,phi):
        if (gcd(i,phi) == 1) :
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
def find_inverse(e,phi):
    m = phi
    x = 1
    y = 0

    if(phi == 1) : return 0
    while (e > 1) :
        q = e//phi
        t = phi

        phi,e,t = e%phi,t,y
        y,x = x-q*t,t
    
    if (x<0) : x+= m
    return x

'''
    Generates public and private keys for RSA
    Parameters :
        None
    
    Returns :
        A list [(n,e),(d,n)] containing the public and the private keys
'''
def generate_RSA(min,max):
    p,q = generate_prime(min,max),generate_prime(min,max)

    n = p*q
    phi = (p-1) * (q-1)
    e = find_coprime(phi)

    d = find_inverse(e,phi)
    return [[n,e],[d,n]]

'''
    Encrypts a message using RSA
    Parameters :
        - msg : the message to encrypt
        - key : the public key (n,e)

    Returns :
        The encrypted message
'''
def encrypt_RSA(msg, key):
    cyphered = ""
    for c in msg:
        cyphered += chr(quickExponent(ord(c),key[1]) % key[0])

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
    raw = ""
    for c in msg:
        raw += chr(quickExponent(ord(c),key[0]) % key[1])
    
    return raw

'''
    TESTS
'''
def main() : 
    print(generate_RSA(4,8))
    return

if __name__ == "__main__" :
    main()