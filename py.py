
i = 1
while i < 2:
    nev = input("Add meg a felhasználóneved: ")
    jelszo = input("Add meg a jelszavad: ")

    if (nev == "bori99") and (jelszo == "Szivecske"):
        print("Sikeres bejelentkezés")
        i+=1
    else:
        print("Sikertelen bejelentkezés")
