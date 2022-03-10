prim = int(input("Irj be egy szamot : "))
if prim > 1:
    for i in range(2,prim):
        if (prim % i) == 0:
            print("Nem prím!")
            break
    else:
        print("Prím!")
else:
    print("Nem prím!")
        


