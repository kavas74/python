szam1 = int(input("Kérem az első számot: "))
szam2 = int(input("Kérem a a második számot: "))

lista = []


for i in range(szam1, szam2):
    if i % 2 == 0:
        lista.append(i)


del lista[0]
print("A két érték közötti páros számok: ",lista)
