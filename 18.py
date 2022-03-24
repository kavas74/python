import random
i = int(input("Mennyi pörgetést tervezünk? "))

v = i

for v in range(i):
    b = input("Mit tippelsz?")
    elv = random.randint(0,5)
    if elv == 3:
        print("Fej")
    else:
        print("Irás")
