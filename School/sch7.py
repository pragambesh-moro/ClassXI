a = input("enter a line: ")
uc = lc = dig = al = 0
for i in a:
    if i.isupper():
        uc += 1
    elif i.islower():
        lc += 1
    elif i.isalpha():
        al += 1
    elif i.isdigit():
        dig += 1
print("UC: ", uc)
print("LC: ", lc)
print("DIG: ", dig)
print("Alpha: ", al)