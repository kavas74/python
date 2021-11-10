# MODULOK

# FÜGGVÉNYEK

def okori(sz):
    s = ""
    szamok = [[10000, 'Y'],[5000, 'J'],[1000, 'M'],
              [500, 'D'],[100, 'C'],[50, 'L'],
              [10, 'X'],[5, 'V'],[1, 'I']]

    i = 0
    while(sz > 0):
        if(sz >= szamok[i][0]):
            s += szamok[i][1]
            sz -= szamok[i][0]
        else:
            i += 1
    return(s)


def kozepkor(sz):
    s = ""
    szamok = [[10000, 'Y'],[5000, 'J'],[1000, 'M'],
              [500, 'D'],[100, 'C'],[50, 'L'],
              [10, 'X'],[5, 'V'],[1, 'I']]

    i = 0
    while(sz > 0):
        if(sz >= szamok[i][0]):
            s += szamok[i][1]
            sz -= szamok[i][0]
        else:
            i += 1
    return(s)

# PROGRAMTÖRZS

szam = int(input("Kérek egy egész számot : "))

print("A {0} szám ókori romai számokkal : {1}".format(szam, okori(szam)))
# print("A {0} szám ókori romai számokkal : {1}".format(szam, kozepkori(szam)))
