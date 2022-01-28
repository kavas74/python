i = 1
while i < 2:
    nev = input("Neved: ")
    if nev == "":
        i+=1
        break 
        
    number = int(input("Mennyit gyüjtött?"))

    if 10 > number:
        print(nev, "Zsenge")
        i += 1
    elif number > 20:
        print(nev, "Nagy koponya")
        i += 1
    else:
        print(nev,"Gyüjtögető")
        i += 1
        
        


