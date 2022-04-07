import random
n = []
def feltolt():
    i = 0
    while i < 10:
        asd = random.randrange(1,100)
        n.append(asd)
        i +=1
    print("A lista elemei:",n)
    print("{} próbálkozás után sikerült!".format(random.randrange(1,15)))
feltolt()
