i = 1
while i < 2:
    felhaszn = input("Ird be a felhasználó neved: ")
    jelszo = input("Ird be a jelszavad: ")
    if (felhaszn == "bori99") and (jelszo == "Szivecske<3"):
        print("Belépés engedélyezve!")
        i += 1
    else:
        print("Belépés megtagadva!")

