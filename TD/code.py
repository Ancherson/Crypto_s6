# Python program to generate the z_i sequence and encrypt messages with their given position

def z(n):
    if n < 0:
        raise AssertionError("Negative index") # Negative index
    elif n == 0:
        return 3 # Cas de base
    else:
        return (2*z(n-1) + 4) % 8

def to_byte_array(x):
    return [x//4, (x - 4*(x//4) - x%2)//2, x%2]

def xor(a, b):
    return int ((a or b) and not (a and b))

def encrypt(msg, pos):
    if not (0 <= msg < 8):
        raise AssertionError("Message is not a correct integer between 0 included and 8 excluded")
    msg_bin = to_byte_array(msg)
    z_bin = to_byte_array(z(pos))
    # We use the duality of boolean and 0-1 integers in Python
    for i in range(3):
        print(xor(msg_bin[i], z_bin[i]), end="") # Calculate bit per bit
    print(" ", end="") # Trailing space to separate each 3-bit block

# Checking the exercise values
encrypt(4, 0)
encrypt(7, 1)
encrypt(1, 2)
encrypt(1, 3)
encrypt(1, 4)
encrypt(6, 5)
encrypt(3, 6)