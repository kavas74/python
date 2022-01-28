print("Egyenleged : 25000FT")
i = 1
while i < 2:
    type = input("Ird be mit szeretnel venni: ")
    keret = int(input("Ird be mennyiért szeretned venni!"))
    if type == "ZX Spectrum":
        print("Működik a gép!")
    else:
        print("Nem működik a gép!")
        break

    if keret <= 25000:
        print("Megtudod venni!")
        megveszed = input("Megveszed?: ")
        lista.append(megveszed)
        i+=1
        print("Megvetted a gépet!")
    else:
        print("Nemtudod megvenni!")
        break


