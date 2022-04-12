


#programtörzs

osszesen = 0
for i in range(1,11):
    s = f"A {i}. megállónál felszállók száma : "
    felszallok = int(input(s))

    osszesen += felszallok

print(f"Az iskolánál {osszesen} tanuló fog leszállni  a buszról.")
print(f"A megállókban átlagosan felszálló tanulók száma {osszesen/10} fő.")
