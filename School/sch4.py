import math as m
x = float(input("Enter X: "))
n = float(input("Enter N: "))
a, b, Sum = 0, 0, 0 
for i in range (1, n+1):
    if i % 2 == 0:
        a += m.pow(x, n)/m.factorial(n)
    elif i % 2 != 0:
        b -= m.pow(x, n)/m.factorial(n)
Sum = 1 - a + b
print("The Sum is: ", Sum)

"""while True:
    print(eval(input()))"""