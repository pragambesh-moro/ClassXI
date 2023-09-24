import math as m

"""TEMPLATE
Sum = 0
N = int(input("Enter N: "))
for i in range(1, N+1):
    Sum = Sum + term
print("Sum of the series is: ", Sum)
"""
while True:
    print("Welcome to Series!")
    print("1. Arithmetic Series 1+2+3+.....N")
    print("2. X^1 + X^2 + .... +N")
    print("3. X^1/1! + X^2/2! - x^3/3! + x^4/4! - .... N")
    ch = int(input("Enter Choice: "))
    if ch == 1:             #1+2+3+....+N
        print("1+2+3+.....N")
        Sum = 0
        a = 1
        N = int(input("Enter N: "))
        for i in range(1, N+1):
            Sum = Sum + a
            a += 1
        print("Sum of the series is: ", Sum)
        print()
    elif ch == 2:           #X^1 + X^2 + .... +N
        print("X^1 + X^2 + .... +N")
        Sum = 0
        a = 1
        x = int(input("Enter X: "))
        N = int(input("Enter N: "))
        for i in range(1, N+1):
            Sum = Sum + m.pow(x, a)
            a += 1
        print("Sum of the series is: ", Sum)
        print()
    elif ch == 3:           #X^1/1! + X^2/2! - x^3/3! + x^4/4! - .... N
        print("X^1/1! + X^2/2! - x^3/3! + x^4/4! - .... N")
        Sum = 0
        a = 1
        sign = +1
        x = int(input("Enter X: "))
        N = int(input("Enter N: "))
        for i in range(1, N+1):
            Sum = Sum + ((m.pow(x, a)/m.factorial(a))*sign)
            sign *= -1
            a += 1
        print("Sum of the series is: ", Sum)
        print()
    else:                   #Break           
        break