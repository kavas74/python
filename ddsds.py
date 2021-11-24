
# modulok

import random

# függvények

def feltolt(v):
    for i in range(0,100):
        v.append(random.randint(0,100))

def kiir(v):
    for i in range(0,len(v)):
        print(v[i], end='\t')

def osszeg(v):
    s = 0
    for i in range(0,len(v)):
        s += v[i]
    return(s)

def paros(x):
    return((x % 2) == 0)

def paratlan(x):
    return((x % 2) > 0)

def megszamlalas(v):
    s = 0
    for i in range(0,len(v)):
        if paros(v[i]):
            s += 1
    return(s)

def megszamlalas2(v):
    s = 0
    for i in v:
        if paros(i):
            s += 1
    return(s)

def legkisebb(v):
    s = 0
    for i in range(1, len(v)):
        if v[i] < v[s] :
            s = i
    return(s)

def legnagyobb(v):
    s = 0
    for i in range(1, len(v)):
        if v[i] > v[s] :
            s = i
    return(s)

def paros_kiir(v):
    for i in range(0,len(v)):
        if paros(v[i]) :
            print(v[i], end=" ")

# programtörzs

v = []

feltolt(v)
kiir(v)

print("A számok összege : {0}.".format(osszeg(v)))
print("A páros számok száma : {0}.".format(megszamlalas(v)))
print("A páratlan számok száma : {0}.".format(megszamlalas2(v)))
print("A legkisebb a {0} elem, értéke {1}.".format(legkisebb(v), v[legkisebb(v)]))
print("A legnagyobb a {0} elem, értéke {1}.".format(legnagyobb(v), v[legnagyobb(v)]))
print("A páros számok: ")
paros_kiir(v)
