szo = input("Irj be valamit: ")

x=set()

vege = ''

for i in szo:
    if i not in x:
        x.add(i)
        vege=vege+str(szo.count(i))+i


print("A karakterekből ennyi darab van:" +vege)
