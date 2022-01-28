
#varos nev;országkód;szelesseg;hosszusag\n



#modulok
#-nincs

#osztályok

class Varos:
    def __init__(self, sor):
      elemek = sor.strip("\n").split(";")
      self.varos = elemek[0]
      self.orszagkod = elemek[1]
      self.szelesseg = elemek[2]
      self.hosszusag = elemek[3]


#függvények
def betoltes():
    f = open("varosok.txt","r")

    while True:
        sor = f.readline()
        if sor == "":
            break
        else:
            elemek = sor.strip("\n").split(";")
            v = {}
            v["varos"] = elemek[0]
            v["orszagkod"] = elemek[1]
            v["szelesseg"] = elemek[2]
            v["hosszusag"] = elemek[3]
            varosok.append(v)
    f.close()




def betoltes2():
    f = open("varosok.txt","r")

    while True:
        sor = f.readline()
        if sor == "":
            break
        else:
            varosok.append(Varos(sor))
    f.close()
    

def kiiras():
    for v in varosok:
        print("---------------------")
        print("Város : {0} ({1}).".format(v["varos"], v["orszagkod"]))
        print("Szélesség : {0}.".format(v["szelesseg"]))
        print("Hosszúság : {0}.".format(v["hosszusag"]))
        print("=====================")



def kiiras2():
    for v in varosok:
        print("---------------------")
        print("Város : {0} ({1}).".format(v.varos, v.orszagkod))
        print("Szélesség : {0}.".format(v.szelesseg))
        print("Hosszúság : {0}.".format(v.hosszusag))
        print("=====================")
#programtörzs



varosok =  []
betoltes2()
kiiras2()
