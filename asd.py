#modulok

#osztályok

#függvények

def maganhangzok_szama(szo) :
    mh = "aáeéiíoóuúüű"
    mh += mh.upper()

    db = 0
    for b in mh:
        db += szo.count(b)
    return(db)


def massalhangzok_szama(szo) :
    mh = "bcdfghjklmpqrstwxyz"
    mh += mh.upper()

    db = 0
    for b in mh:
        db += szo.count(b)
    return(db)

def szokozok_szama(szo):
    return(szo.count(" "))


def karakterenkenti_statisztika(szo):
    betuk = "aáeéiíoóuúüűbcdfghjklmpqrsvtwxyz"
    betuk += betuk.upper()

    kars = []
    for b in betuk:
        kars.append([b, szo.count(b)])
    return(kars)


def statisztika_megjelenitese(stat):
    for i in stat:
        if(i[1] > 0):
            print(f"{i[0]} : {i[1]}")





#programtörzs
nev = input("Név: ")

print(f"A név hossza : {len(nev)} karakter.")
print(f"A Mássalhangzók száma: {massalhangzok_szama(nev)}db.")
print(f"A Magánhangzók száma: {maganhangzok_szama(nev)}db.")
print(f"A szóközök száma: {szokozok_szama(nev)}db.")


k=karakterenkenti_statisztika(nev)
statisztika_megjelenitese(k)
