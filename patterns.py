while True:
    print("Welcome to patterns!")
    print("1. Right facing arrow")
    print("2. Upward 90")
    print("3. Downward 90")
    print("4. Multiplication Pattern of a given number")
    print("n. Cube")
    print("6. Right Side Triangle ->INC")
    print("7. Right Sided Triangle -> DEC")
    print("8. Hill")
    print("9. Reverse Hill")
    print("10. Diamond")
    ch = int(input("Enter choice: "))
    n = int(input("Enter N: "))
    if ch == 1:                         #Right Arrow
        #Upper Half
        for i in range(n):
            for j in range(1, i+1):
                print("*", end = " ")
            print()
        #Lower Half
        for x in range(n, 0, -1):
            for y in range(x+1, 1, -1):
                print("*", end = " ")
            print()
    elif ch == 2:                       #Upward 90
        for i in range(n):
            for j in range(i+1):
                print("*", end = " ")
            print()
    elif ch == 3:                       #Downward 90
        for i in range(n):
            for j in range(i, n):
                print("*", end = " ")
            print()
    elif ch == 4:                       #Multiplication Pattern 
        n = int(input("enter n: "))
        for i in range(1, n+1):
            print()
            for j in range(1, n+1):
                print(i*j, end = " ")
        print()
    elif ch == 5:                       #Cube
        for i in range(n):
            for j in range(n):
                print("*", end = " ")
            print()
    elif ch == 6:                       #Right Side Triangle -> INC
        for i in range(n):
            for j in range(i, n):
                print(" ", end = " ")
            for j in range(i+1):
                print("*", end = " ")
            print()
    elif ch == 7:                       #Right Sided Triangle ->DEC
        for i in range(n):
            for i in range(i+1):
                print(" ", end = " ")
            for i in range(i, n):
                print("*", end = " ")
            print()
    elif ch == 8:                       #Hill
        for i in range(n):
            for j in range(i, n):
                print(" ", end = " ")
            for j in range(i):
                print("*", end = " ")
            for j in range(i+1):
                print("*", end = " ")
            print()
    elif ch == 9:                       #Reverse Hill
        for i in range(n):
            for j in range(i+1):
                print(" ", end = " ")
            for j in range(i, n-1):
                print("*", end = " ")
            for j in range(i, n):
                print("*", end = " ")
            print()
    elif ch == 10:                      #Diamond
        for i in range(n-1):              #Upper Half
            for j in range(i, n):
                print(" ", end = " ")
            for j in range(i):
                print("*", end = " ")
            for j in range(i+1):
                print("*", end = " ")
            print()
        for i in range(n):              #Lower Half
            for j in range(i+1):
                print(" ", end = " ")
            for j in range(i, n-1):
                print("*", end = " ")
            for j in range(i, n):
                print("*", end = " ")
            print()
    else:                               #BREAK
        print("Exit")
        break
