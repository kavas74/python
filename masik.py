class HiresNo:
    def __init__(self,nev, foglalkozas, nemzetiseg):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nemzetiseg = nemzetiseg
    def elonev(self):
        if self.nemzetiseg == "a":
            return("Ms.")
        else:
            return("Frau")

#programtörzs


nok = []
for i in range(0,3):
    nev = input("Add meg egy hires nő nevét!")
    fogl = input("Add meg a foglakozását!")
    nemz = input("Add meg  a nemzetiségét (a/n)!")

    no = HiresNo(nev, fogl, nemz)
    nok.append(no)

for i in range(0,3):
    print(f"{nok[i].elonev()} {nok[i].nev} egy hires {nok[i].foglalkozas}")
