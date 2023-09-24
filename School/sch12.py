n = int(input("enter a number: "))
if n > 1:
    for i in range(2, n):
        if (n%i == 0 and n != i):
            print(n, " is a composite number")
            break
        else:
            print(n, " is a prime number")
            break
elif n == 0 or 1:
    print(n, " is neither prime nor composite")
else:
    print(n, "is a composite number")