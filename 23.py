import random
lista = []

for i in range(10):
    valami = random.randint(1,10)
    lista.append(valami)


a = int(input("Adj meg egy számot: "))
b = lista.count(a)
print("A szám ennyiszer szerepel a listában:  {}".format(b))
print("Lista további elemei: {}".format(lista))
