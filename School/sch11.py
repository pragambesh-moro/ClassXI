s = input("Enter a string: ")
n = len(s)
c = 0
for i in range(n):
    if s[i].isspace():
        c += 1
print(c)