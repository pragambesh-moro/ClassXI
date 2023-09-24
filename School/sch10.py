s1 = input("Enter a string: ")
le = len(s1)
print("Original string is: ", s1)
s2 = " "
for a in range(le):
    if a % 2 == 0:
        s2 += s1[a]
    else:
        s2 += s1[a].upper()
print(s2)