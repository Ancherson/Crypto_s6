'''
    Bit stuffs a text in order to make its length a multiple of 16
    Parameter :
        - The raw text
    Returns :
        The bit stuffed raw text
'''
def stuffing(rawtext):
    if len(rawtext) == 16 :
        rawtext += 16*chr(16)
    else : 
        r = len(rawtext) % 16
        rawtext += (16-r)*chr(16-r)
    return

def encrypt_hybrid():
    return