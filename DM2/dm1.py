import random
import collections
import numpy as np 
############################ Vernam #############################

# Question 1 :


# On défini une fonction xor

def xor(d,k):
    bin_d= [ord(i) for i in d] #on transforme d le message en tableau de int
    bin_k= [ord(e) for e in k] #on transforme la clef k en tableau de int
    res= ""
    for i in range (0,len(bin_d)):
        res += chr(bin_d[i]^bin_k[i]) #l'opération xor
    return res

def G():
    key= ""
    for i in range(0, 4):
        key+= str(random.randint(0,9)) #répartition uniforme grâce à randint (on le limite entre 0 et 9 pour avoir 4 char)
    return key

def E(data, key):
    print("Texte clair : "+data+"\n")
    datac=""
    i=0
    while(len(datac)<len(data)): #on encode sur tout le texte
        if 4+i<len(data): # dci=di^ki(mod 4)
            datac += xor(data[i:4+i], key)
        else:
            datac += xor(data[i:len(data)], key)
        i+=4
    print("Texte chiffré avec la clef ("+key+") : "+datac+"\n")
    return datac

def D(datac, key): # même principe que encode
    print("Texte chiffré : "+datac+"\n") 
    data= ""
    i=0
    while(len(data)<len(datac)):
        if 4+i<len(datac):
            data += xor(datac[i:4+i], key)
        else:
            data += xor(datac[i:len(datac)], key)
        i+=4
    print("Texte clair : "+data+"\n")
    return data

# Question 2 :
"""
        Une méthode de cryptoanalyse qui semble adatpée pour un problème du type de Vernam
    est l'attaque par analyse de fréquence. Elle consiste a prendre un texte clair dans la langue
    dont laquelle le message est chiffré et étudier les différentes fréquences d'apparition des lettres.
        Puisque notre clef est générée aléatoirement de manière uniforme et ne change pas le chiffrement doit
    conserver la répartition des fréquences. Ainsi par comparaison nous pourrons déchiffer les message.

"""
# Question 3 :

def ind_du_plus_proche(l, val):
    l= np.asarray(l)
    ind= (np.abs(l - val)).argmin()
    return ind

def attaque_analyse_freq(t, langue):
    alphabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #tableau de fréquence des lettres en français trouvé sur internet 
    freqFr= [9.42, 1.02, 2.64, 3.39, 15.87, 0.95, 1.04, 0.77, 8.41, 0.89, 0.00, 5.34, 3.24, 7.15, 5.14, 2.86, 1.06, 6.46, 7.90, 7.26, 6.24, 2.15, 0.00, 0.30, 0.24, 0.32]
    #tableau de fréquence des lettres en anglais trouvé sur internet
    freqAng= [8.08, 1.67, 3.18,	3.99, 12.56, 2.17, 1.80, 5.27, 7.24, 0.14, 0.63, 4.04, 2.60, 7.38, 7.47, 1.91, 0.09, 6.42, 6.59, 9.15, 2.79, 1.00, 1.89, 0.21, 1.65, 0.07]
    freqT= [t.count(char) for char in t] #tableau de fréquence pour notre texte
    res=""
    for i in range(len(freqT)):
        freqT[i]=freqT[i]/len(freqT)*100
    if langue=="anglais": #on va comparer les fréquences des lettres en fonction de la langue de notre texte et lui assigner une lettre
        for i in freqT:
            res+=alphabet[ind_du_plus_proche(freqAng, i)]
    elif langue=="francais":
        for i in freqT:
            res+=alphabet[ind_du_plus_proche(freqFr, i)]
    return res
    
def testC3(T, l, langue):
    count=0
    for i in range(100):
        key=G()
        a=random.randint(0,len(T))
        b=a+l
        t=T[a:b]
        t_sans_espace=t.replace(" ","")
        c=E(t_sans_espace,key)
        ac=attaque_analyse_freq(c, langue)
        if ac==t_sans_espace:
            count+=1
    print(count)
    return (count>= 50)

############################## C3 ####################################################
import time
import math
from Crypto.Cipher import AES


 			#Fonctions utiles



def puissance2(n):    #trouve la puissance de 2 juste avant n
	res = 0
	while 2**res < n:
		res = res + 1
	return res-1

def pgcd(a,b):        #calcule le pgcd
	while b != 0:
		tmp = b
		b = a%b
		a = tmp
	return a

def generer_premier(n):   #calculer le plus petit nombre premier avec n
	res = 2
	while pgcd(res, n) != 1:
		res = res + 1
	return res


 			#QUESTION 1


def temoin_miller(n,a):
	sval = 0
	dval = 0
	for s in range (1,puissance2(n-1)):
		for d in range (n//s):
			if n-1 == pow(2,s) * d:     # pas efficace mais je vois pas comment mieux faire
				sval = s
				dval = d
				break
	x = a**dval % n
	if x == 1 or x == n-1:
		return False
	for i in range(sval-1):
		x = (x**2) % n
		if x == n-1:
			return False
	return True

def Miller_Rabin(n,k):        #algorithme de miller_rabin
	if n == 2 or n == 3:
		return True
	if n%2 == 0 or n<2:
		return False
	for i in range(k):
		a = random.randint(1, n-2)
		if temoin_miller(n,a):
			return False
	return True


			 #QUESTION 2


def euclide(e,phi):           #permet de trouver d pour la clef rsa
	print(e,phi)
	res = 1
	while ((res*e)%phi) != 1:
		res = (res+1)
	return res


def rsa_clef():   
	p = 0
	q = 0     											       
	while not(Miller_Rabin(p,100) and Miller_Rabin(q,100)):    # on veut p et q premiers
		p = random.randrange(2,1000)                           # 1000 = grande valeur choisie aleatoirement
		q = random.randrange(2,1000)
		while q == p:										   # q et p doivent etre différents
			q = random.randrange(2,10000)
	n = p*q
	phi = (p-1)*(q-1)
	e = generer_premier(phi)     
	d = euclide(e,phi)
	return [e,n,d]


def rsa_chiffrement(m,e,n):       #on applique la formule pour le chiffrement
	res = (pow(int(m),e)) 
	return (res%n)


def rsa_dechiffrement(c,d,n):     #on applique la formule pour le déchiffrement
	res = (pow(int(c),int(d)))
	return (res%n)


    		 #QUESTION 4

def bourrage(x):
	m = str(x)              
	if len(m) == 16:
		return m
	else:
		if len(m)%2 == 1:          #on ajoute un 0 en plus si c'est impair pour bien avoir 16 bytes
			m = m + "0"
		nb_bytes = int(len(m)/2)       #un octet est sur deux caracteres, donc on divise par 2 pour savoir combien d'octet bourrer
		ajout = ('0' + str(8-nb_bytes)) * (8-nb_bytes-1)
		res = m + "0x" + ajout
		return res

			 #QUESTION 	5

def xor1(m,k):
    tab = [int(d) for d in m]           #on transforme m et k en tableau de int pour xorer
    tab_clef = [int(e) for e in k]
    res = ""
    for i in range (0,len(tab)):
        res = res + str(tab[i]^tab_clef[i])    
    return res


def hybride(m):
	clef_rsa = rsa_clef()                  
	k = rsa_chiffrement(m,clef_rsa[0],clef_rsa[1])     #on generer une clef publique avec le chiffrement rsa
	tab = [m[i:i+16] for i in range(0, len(m), 16)]    #on decoupe m en bloc de 16
	res = ""
	for i in range (0,len(m)):                          
		res = res + xor1(aes_encryption(bourrage(tab[i]),k),tab[i])   #on xor l'encryption aes de m et de la clef rsa generé avec tab[i] comme dans la formule 
	return res                                  


def aes_encryption(m,k):     #code de la bibliothèque pycryptodom pour encrypt en AES
	cipher = AES.new(bourrage(k).encode("utf8"), AES.MODE_EAX)
	nonce = cipher.nonce
	ciphertext,tag = cipher.encrypt_and_digest(bourrage(m))
	return ciphertext



    	#6

def pollard(pq):
	x = 2
	y = 2
	while pgcd(x-y,pq) == 1 or x == 2:
		x = (x*x+1)%pq
		y = ((y*y+1)*(y*y+1)+1)%pq
		print (x,y)
	return pgcd(x-y, pq)

############################# C 8 #####################################################


		#1
def compression(x,k):  # on applique la formule de davies-Meyer
    return xor1(aes_encryption(k,x),k)


    	#2

def hachage(x):
    m = str(x)
    tab = [m[i:i+16] for i in range(0, len(m), 16)]  #on decoupe en bloc de 16
    res =  "0"*16                                    #on initialise avec 16 zero
    for i in range (len(tab)):						 #on applique compression sur chaque bloc		 
        res = (compression(tab[i],res))		
    return res

		#3 

def verify(m1,m2) :
	signature = aes_encryption(m1)
	return (signature[1] == hachage(m2))



	########## TEST ##########

def test(): 

    print("TP5")
    print("QUESTION 1:")
    print("3 est-il premier? ")
    if (Miller_Rabin(3,1000) == True):
        print("Oui")
    else:
        print("Non")
    i = random.randrange(1000,1000000000)
    print(str(i) + " est-il premier? ")
    if (Miller_Rabin(i,1000) == True):
        print("Peut-être")
    else:
        print("Non")

    """
    for i in range(20):
        print(i)
        print(Miller_Rabin(i,1000))
    """
    print('\n')
    
    print("Question 2:")
    clef_rsa = rsa_clef()
    m = 163
    e = clef_rsa[0]
    n = clef_rsa[1]
    d = clef_rsa[2]
    print("e = " + str(e))
    print("n = " + str(n))
    print("d = " + str(d))

    res1 = rsa_chiffrement(m,e,n)
    print("message: " + str(m) + " chiffrement rsa:" + str(res1))
    print("dechiffrement rsa: " + str(rsa_dechiffrement(res1,d,n)))
    print('\n')

    print("Question 4:")
    m = "1155"
    print("message: " + m + ", bourrage: " + bourrage(m))
    print('\n')

    """
    print("Question5:")
    print(hybride("124578326598135"))
    print('\n')
    """

    print("Question6:")
    pq = 2**56 + 100
    res = pollard(pq)
    print("pq = 2⁵⁶ + 100, factorisation de Pollard: " + str(res) + " * " + str(pq/res))
    

    #on a pas réussi à faire marcher la fonction aes, donc on a pas pu tester les questions du tp8

    # mais on a laissé le code qu'on a essayé de faire

test()


############################ Partage de secret #########################################


from math import ceil, sqrt

def test_primalite(p):
    k=ceil(sqrt(p))
    for i in range (2, k+1):
        if p%i==0:
            return False
    return True

def generate(m, k, s):
    p=m
    while test_primalite(p):
        p+=1
    coefficients= [random.randrange(0, p-1) for _ in range(k)] # on tire au hasard les coefficients
    coefficients.append(s)
    return(p, coefficients)

##############################################################


def polynom(x, p, coefficients): # pour évaluer les polynômes de 1 à m
    point = 0
    for coefficient_index, coefficient_value in enumerate(coefficients[:len(coefficients)-1], start=1):
        point += coefficient_value * pow(x,coefficient_index)
    return (point+coefficients[-1])%p

def distribute(m, p, coefficients): # crée les parts de secret pour chaque agent
    si = []
    for x in range(1, m+1):
        si.append((x, polynom(x, p, coefficients)))
    return si

###############################################################

def calc_inverse(a,b): #implémente l'algorithme d'euclide
    r=a
    u=1
    v=0
    r_suivant=b
    u_suivant=0
    v_suivant=1
    while r_suivant!=0:
        quotient=r//r_suivant
        r=r_suivant
        u=u_suivant
        v=v_suivant
        r_suivant=r-q*r_suivant
        u_suivant=u-q*r_suivant
        v_suivant=v-q*r_suivant
    return u
    

def coalition(k, p, Si): 
    somme = 0
    for (i,si) in Si:
        numerateur, denominateur=1,1
        for (j,sj) in Si:
            if j != i:
                numerateur*=-j
                denominateur*=i-j
        somme +=(si*(numerateur*calc_inverse(denominateur,p))%p) # formule de lagrange
    return int(somme%p)
