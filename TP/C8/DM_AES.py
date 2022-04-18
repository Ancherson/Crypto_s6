import random
from Crypto.Cipher import AES
from C5.RSA import generate_RSA

cipher = AES.new(random.randbytes(16))

'''
    Davies-Meyer's compressing function
'''


def davies_meyer(x, y):
    return


'''
    Merkle_Damguard's Hashing function
'''


def hash_merkle_damguard(text):
    return


'''
    Signature using hashing
'''


def sign_RSA(text):
    keys = generate_RSA()
    cyphered = hash_merkle_damguard(text)

    # keys[1] = (d,n)
    signature = pow(cyphered, keys[1][0]) % keys[1][1]
    return signature


'''
    Signature verification
    Parameters :
        - The cyphered text 
        - The signature sign
        - The public key pub_key = (n,e) from RSA
'''


def verify_RSA(text, sign, pub_key):
    return hash_merkle_damguard(text) == pow(sign, pub_key[1]) % pub_key[0]
