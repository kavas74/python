def haromszog():
    i = 0
    while i < 1:
        egyik = int(input("Háromszög egyik oldal: "))
        masik = int(input("Háromszög másik oldal: "))
        masik2 = int(input("Háromszög harmadik oldal: "))
        if egyik > masik:
            egyik,masik = masik,egyik
        if egyik > masik2:
            egyik,masik2 = c,egyiks
        if masik > masik2:
            masik,masik2 = masik2,masik
        if egyik*egyik +  masik*masik == masik2*masik2:
            print("Derékszögű")
        else:
            print("Nem derékszögű")
        i+=1
haromszog()
    
