i = 0

while True:
    szam = float(input("Mennyit ittal ma? "))
    i += szam
    print("Eddig {0:.0f} deci vizet ittal meg!".format(i))

    if szam == 0:
        print("0 át nem adhatsz meg!")
        break
    
    if i >= 25:
        print("2,5 litert már ittál!")

    if i >= 35:
        print("3,5 litert már ittál!")
        break
        
