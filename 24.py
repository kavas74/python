import random
lista = []

for i in range(10):
    valami = random.randint(1,10)
    lista.append(valami)


a = int(input("Adj meg egy számot: "))
b = lista.count(a)
hanyadik = lista.index(a)
print("A szám ennyiszer szerepel a listában:  {}".format(b))
print("A tömb elemei: {0}".format(lista))
print("A megadott szám a listának {0} eleme".format(hanyadik))
