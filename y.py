

#osztalyok


class Bolygo:

  # ---------------
  # konstruktor :
  # ---------------
  def __init__(self,s):
    elemek = s.strip('/n').split(';')

    self.megnev = elemek[0]          # bolygó megnevezése
    self.a = float(elemek[1])        # főtengely [CSE]
    self.e = float(elemek[2])        # excentritás
    self.fi = float(elemek[3])       # pályaelhajlás [fok]
    self.Y_szid = float(elemek[4])   # sziderikus év [nap]
    self.Y_szin = float(elemek[5])   # szinódikus év [nap]
    self.r_e = float(elemek[6])      # egyenlítő sugara [km]
    self.l = float(elemek[7])        # lapultság
    self.m = float(elemek[8])        # tömeg [földtömeg]
    self.ro = float(elemek[9])       # sűrűség [g/cm3]
    self.g = float(elemek[10])       # gravitációs gyorsulás [m/s2]
    self.P = float(elemek[11])       # felszíni nyomás [bar]

  # -----------------
#fuggvenyek

def betoltes():
    f = open("bolygok.txt", "r")

    while True:
        sor = f.readline()
        if sor == "":
            break
        else:
            bolygok.append(Bolygo(sor))

    f.close()

def feladat4():
    print("4. feladat")
    for i in range(0,9):
        if bolygok[i].P == 0.0:
            print(bolygok[i].megnev)
#programtörzs
  
bolygok = []

betoltes()

bolygok[2].g = 9.82
bolygok[6].r_e = 60268
print(len(bolygok))

feladat4()

