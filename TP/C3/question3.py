'''
Réponse question 2:
    On procède par analyse fréquentielle.
'''

### DEBUT DU FICHIER POUR LA QUESTION 3

from random import randint
from question1 import G,E

def read_text(filepath):
    f = open(filepath,"r")
    return f.read()

def decrypt(c):
    # TODO
    return 

def q3_long(l,nbtest):
    postest = 0
    T = read_text("./longText.txt")
    for i in range (nbtest):
        k = G()
        r = randint(0,T-l)
        t = T[r:r+l]
        c = E(t,k)
        d = decrypt(c)
        if (d == t):
            postest+=1
    if(postest>= nbtest//2):
        q3_long(l//2,nbtest)
    else :
        return l


