lista = []
i = 0
osszeg = 0
paros = []
paratlan = []
for i in range(i,100):
    szam = int(input("Adjon meg egy számot: "))
    osszeg = osszeg + szam
    if (szam % 2 == 0):
        paros.append(szam)
    if (szam % 2 != 0):
        paratlan.append(szam)
    if (osszeg >= 100):
        break
szamolas = len(paros)
szamolas2 = len(paratlan)
print("{0} páros és {1} páratlan szám van!".format(szamolas,szamolas2))
        
        
    
    
