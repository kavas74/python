lista = []
paros = []
paratlan = []
i = 1
while i < 6:
    szam = int(input("Irj be egy számot: "))
    if -99 <= szam <= 99:
        print("Rendben!")
        i += 1
        lista.append(szam)
        if (szam % 2 == 0):
            paros.append(szam)
        if (szam % 2 != 0):
            paratlan.append(szam)
    elif -99 > szam > 99:
        print("Rossz")
    else:
        print("Ird be ujra a számot :")



szamolas = len(paros)
szamolas2 = len(paratlan)

if szamolas == 0:
    print("Nincs páros szám")

if szamolas2 == 0:
    print("Nincs páratlan szám")

        
print("{0} páros és {1} páratlan szám van".format(szamolas,szamolas2))
