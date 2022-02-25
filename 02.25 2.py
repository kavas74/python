import random
n = []
lista = int(input("Hany elemű legyen a lista: "))
def feltolt():
    i = 0
    while i < lista:
        asd = random.randrange(1,100)
        n.append(asd)
        i +=1
    print("A lista elemei:",n)
feltolt()

def kisebbnagyobb():
    kisebb = min(n)
    nagyobb = max(n)
    if (kisebb!=nagyobb):
        print("A legkisebb szám a:",kisebb)
        print("A legnagyobb szám a:",nagyobb)
    else:
        print("Egyenlő")
kisebbnagyobb()
