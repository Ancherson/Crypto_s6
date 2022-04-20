import random
from Crypto.Cipher import AES
from RSA import generate_RSA
from MR import quickModularExponent

aes = AES.new(random.randbytes(16))

'''
    Davies-Meyer's compressing function
'''


def davies_meyer(B, H):
    return str(ord(aes.encrypt(B)) ^ ord(H))


'''
    Merkle_Damguard's Hashing function
'''


def hash_merkle_damguard(text):
    cyphered = "0000000000000000"
    Hi = "0000000000000000"

    for k in range(16, text.len(), 16):
        Bi = text[k:k+15]
        Hi = davies_meyer(Bi, Hi)
        cyphered += Hi

    return


'''
    Signature using hashing
'''


def sign_RSA(text):
    keys = generate_RSA()
    cyphered = hash_merkle_damguard(text)

    # keys[1] = (d,n)
    signature = quickModularExponent(int(cyphered), keys[1][0], keys[1][1])
    return signature


'''
    Signature verification
    Parameters :
        - The cyphered text 
        - The signature sign
        - The public key pub_key = (n,e) from RSA
'''


def verify_RSA(text, sign, pub_key):
    return hash_merkle_damguard(text) == quickModularExponent(sign, pub_key[1], pub_key[0])


def main():
    return


if __name__ == "__main__":
    main()
