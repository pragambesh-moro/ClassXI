import math as m
#Program to find the sum of the digits of a given number
"""n = int(input("Enter the number: "))
s = 0
while n>0:
    nm = n%10
    s += nm
    n//=10
print(s, " is the sum of the digits of the number.")"""

x = int(input("Enter X: "))
n = int(input("Enter N: "))
a, b, Sum = 0, 0, 0
for i in range (1, n+1):
    if i % 2 == 0:
        a += m.pow(x, n)
    elif i % 2 != 0:
        b -= m.pow(x, n)
Sum = 1 - a + b
print("The Sum is: ", Sum)

"""x = int(input("Enter X: "))
n = int(input("Enter N: "))
sum = 1
i = 1
while i<=n:
    if i % 2 == 0:
        sum += m.pow(x, n)
        i+=1
    elif i % 2 != 0:
        sum -= m.pow(x, n)
        i+=1
print("Sum is: ", sum)"""