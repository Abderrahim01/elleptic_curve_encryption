from ellipticcurve import EllipticCurve
from point import Point,Inf
from gen import Gen
from math import *


modulo=11
c = EllipticCurve(1,6,modulo)
inf = Inf(c)

list_gen = []
for i in range(modulo):
    for y in range(modulo):
        if c.has_point(i, y):
            point = Point(c, i, y)
            p2 = point
            list_point = []
            list_point.append(point)
            while True:
                tmp = point
                point = point + p2
                if point == inf:
                    break
                list_point.append(point)
            list_gen.append(Gen(tmp, (len(list_point) + 1)))

print
print "Liste des point de la courbe :"
for i in list_gen:
    print i

print
print "P =" ,list_gen[0]
P = list_gen[0]

print
print "Calculer l'ensemble G : "
i=1
p2 = inf
list_L = []
while True:
    print str(P.point)," * ",i," = ",str((P.point+p2))
    if (P.point+p2) == inf:
        r = i
        break
    else:
        i = i + 1
        p2 = P.point + p2


print "Ordre = ",r
m = int(round(sqrt(r)))

print "m = ",m

p2 = P.point
for i in range(m-1):
    list_L.append(p2)
    p2 = p2 + P.point
s = -p2

print
print "Liste L :"
for l in list_L:
    print(l)
print "s =",str(s)

print
print "Choix de la cle prive"
q = 5 * P.point

print "Q = ", str(q)



list_j = []
for j in range(1,m-1):
    p3 = (j * s) + q
    if p3 in list_L:
        list_j.append((j,p3))

print
print

print("List j :")
for i, p2 in list_j:
    print i," ",str(p2)

print
print

for i in range(1,m-1):
    for j, p2 in list_j:
        if p2 in list_L and p2 == i*P.point:
            print 'point :', i*P.point
            print "Cle prive : ",((i+m*j)%modulo)