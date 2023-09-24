s = input("Enter a string: ")
l = len(s)
p = l - 1
index = 0
while index < p:
    if(s[index] == s[p]):
        index += 1
        p -= 1
    else:
        print("String is not a palindrome")
        break
else:
    print("string is palindrome")