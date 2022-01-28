i = 1



while i < 2:
    nev = input("Ird be a vizsgázó nevét: ")
    pont = int(input("Ird be a pontszámodat"))

    if nev == "":
        print("Muszály megadnod a nevét a vizsgázónak!")
        break
    if pont == "0":
        print("Muszűly megadnod pontszámot!")
        break
    
    if pont >= 48:
        print(nev,"vizsgája sikeres!")
        i+=1
    else:
        print(nev,"vizsgája sikertelen")
        
