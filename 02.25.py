def function():
    i = 1
    while i < 4:
        a = int(input("Ird be az egyik oldalát a háromszögnek: "))
        b = int(input("Ird be az egyik oldalát a háromszögnek: "))
        c = int(input("Ird be az egyik oldalát a háromszögnek: "))
    
        if a == 0:
            print("AZ A HIBÁS")
        if b == 0:
            print("A B HIBÁS")
        if c == 0:
            print("A C HIBÁS")
            continue

    
        if a > b:
            a,b = b,a
        if a > c:
            a,c = c,a
        if b > c:
            b,c = c,b

        
        if a*a + b*b == c*c:
            print("A %d,%d,%d oldalú háromszög derékszögű"%(a,b,c))
        else:
            print("A %d,%d,%d oldalú háromszög nem derékszögű"%(a,b,c))

        if a*a + b*b < c*c:
            print("A %d,%d,%d oldalú háromszög tompaszögű"%(a,b,c))
        else:
            print("A %d,%d,%d oldalú háromszög nem tompaszögű"%(a,b,c))

        if a*a + b*b > c*c:
            print("A %d,%d,%d oldalú háromszög hegyesszögű"%(a,b,c))
        else:
            print("A %d,%d,%d oldalú háromszög nem hegyesszögű"%(a,b,c))


        terulet = a+b*c
        kerulet = a+b+c

            
        print("A háromszög területe: ",terulet)
        print("A háromszög kerülete: ",kerulet)
        print("Készitette: Varga Milán")
function()
    
