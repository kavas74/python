def function():
    i = 0
    while i < 10:
        szam = int(input("Irj be egy számot: "))
        if (szam % 2 == 0) and (szam % 3 == 0):
            print("Igaz állitás!")
        else:
            print("Hamis állitás!")
        i += 1
function()
