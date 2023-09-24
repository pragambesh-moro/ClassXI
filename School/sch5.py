import math as m
x = int(input("Enter x: "))
n = int(input("Enter n: "))
a, b = 0, 0
for i in range(n+1):
    if i%2==0:
        a+=m.pow(x, i)
    elif i%2 != 0:
        b-=m.pow(x, i)
Sum=a+b
print(Sum, " is the Sum")
