import random
i = int(input("Mennyi nevet akarsz bekerni? "))

v = i
lista = []
for v in range(i):
    nev = input("Add meg a neveket: ")
    lista.append(nev)
    if nev == 0:
        break

print("Tagok akik a sorsolásba szerepelnek:",lista)

randomvalaszt = random.choice(lista)
print("A sorsolás nyertese:",randomvalaszt)
