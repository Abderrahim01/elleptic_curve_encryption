from random import randint
from point import Point, Inf
from ellipticcurve import EllipticCurve
from gen import Gen
from string import ascii_lowercase

##
#
#   Fontions utilise pour le TP
#
##

#				Fonction pour le teste de primalite			#
def isPrime(num):
    for x in range(int(num) - 1, 1, -1):
        if int(num) % x == 0:
            return False


##              Fonction pour chiffrer un message           #
def chiffrer(m, pubR, g):
    k = randint(1, g.get_modulo() - 1)
    inf = Inf(g.point.curve)
    y1 = k * g.point
    y2 = m + (pubR * k)
    while y1 == inf or y2 == inf:
        k = randint(1, g.get_modulo() - 1)
        y1 = k * g.point
        y2 = m + (pubR * k)
    return y1, y2


##              Fonction pour dechiffrer un message         #
def dechiffrer(y1, y2, privR):
    return (y2 + (-y1 * privR))


## Debut du TP
a = 1
b = 6
p = 137

c = EllipticCurve(a, b, p)
inf = Inf(c)
# list_char = ['!','"','#','$','%','&','(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~','[',']']


list_gen = []
## Generer la liste des generateurs avec leur ordre pour une courbe elliptique
for i in range(p):
    for y in range(p):
        if c.has_point(i, y):
            point = Point(c, i, y)
            p2 = point
            #n = 1
            list_point = []
            list_point.append(point)
            while True:
                tmp = point
                point = point + p2
                if point == inf:
                    break
                list_point.append(point)
                #n = n + 1
            list_gen.append(Gen(tmp, (len(list_point) + 1)))

for gen in list_gen:
    print(gen)

## Choix du generateur
gen = list_gen[8]

## Generation des cles pour Alice et Bob
privB, pubB = gen.gen_keys()
privA, pubA = gen.gen_keys()

##Question 1 & Question 2 :
## On cree un message en forme de point eliptirque de la courbe
m = gen.point * 90


print 'Generateur : {}, cle genere pour Bob : {}, {}'.format(str(gen), privB, pubB)
print 'Generateur : {}, cle genere pour Alice : {}, {}'.format(str(gen), privA, pubA)


## Chiffrement du point
y1, y2 = chiffrer(m, pubB, gen)
print 'Message clair {}, Message chiffre : {},{}'.format(m, y1, y2)

message_dechiffre = dechiffrer(y1, y2, privB)
print 'Message chiffre {},{}, Message clair : {}'.format(y1, y2, message_dechiffre)

print
print

##Question 5 :
with open('test', 'r') as f:
    text = f.read()
n = 1
lettre_p = []
for lettre in text:
    n = n + 1
    lettre_p.append((lettre, gen.point * n))

for i, p in lettre_p:
    print(i + ' ' + str(p))

list_ltr_p_c = []
for lettre, ltr_p in lettre_p:
    y1, y2 = chiffrer(ltr_p, pubB, gen)
    print 'Message clair {}, Message chiffre : {},{}'.format(ltr_p, y1, y2)
    list_ltr_p_c.append((y1, y2))

print
print

for y1,y2 in list_ltr_p_c:
    print("{} {}".format(y1,y2))

phrase = ""
for y1, y2 in list_ltr_p_c:
    message_dechiffre = dechiffrer(y1, y2, privB)
    print 'Message chiffre {},{}, Message clair : {}'.format(y1, y2, message_dechiffre)
    for lettre, ltr_p in lettre_p:
        if ltr_p == message_dechiffre:
            print lettre
            phrase = phrase + lettre

print(phrase)

##Question 7 :

print("Donnez cle prive pour dechiffree : ")
privtest = int(input("Entrer cle priv :"))

print("Message a dechiffrer : ")
x1 = int(input("y1_x : "))
y1 = int(input("y1_y : "))
y1_c = Point(c,x1,y1)
x1 = int(input("y2_x : "))
y1 = int(input("y2_y : "))
y2_c = Point(c,x1,y1)

message_dechiffre = dechiffrer(y1_c,y2_c,privtest)
print("Message chiffre {},{}, message en clair : {}".format(y1_c,y2_c,message_dechiffre))

##Question 8 :
'''
list_char2 = list(ascii_lowercase)
list_char2 = list_char2 + ['1', '2', '4', '5', '6', '7', '8', '9', '0', '#', '@', '!', '&', '$', '%']
list_char2.insert(0, '*')

p = 37
c8 = EllipticCurve(2, 9, p)
inf = Inf(c8)

list_point = []
list_gen = []

for i in range(p):
    for y in range(p):
        if c.has_point(i, y):
            point = Point(c, i, y)
            point2 = Point(c, i, y)
            n = 1
            list_point = []
            list_point.append(point2)
            while True:
                point2 = point2 + point
                if point2 == inf:
                    break
                list_point.append(point2)
                n = n + 1
            list_gen.append(Gen(point, (len(list_point) + 1)))
'''
