string2 = input("Ird be a vezetékneved: ")
string = input("Ird be a keresztneved: ")

first_char = ""
first2_char = ""
for i in range(0, 1):
    first_char = first_char + string[i]
for i in range(0, 1):
    first2_char = first2_char + string2[i]



osszead = first2_char + first_char
    
print('Monogram:',osszead)
