def szabalyos(m):
    return(m[0].isupper() and m[-1] in ".!?")


mondat = input("Kérem irjon be egy mondatot: ")
print(f"A mondat hossza {len(mondat)} karakter")

if szabalyos(mondat):
    print("A mondat szabályos.")
else:
    print("A mondat nem szabályos.")
