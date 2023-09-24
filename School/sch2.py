#Program to find reverse/check for palindrome
while True:
    print("1. Reverse a number")
    print("2. Check if its palindrome")
    print("3. exit")
    ch = int(input("Enter a choice: "))
    print()
    if ch == 1:
        str = input("Enter the number: ")
        print()
        new_str = str[::-1]
        print(new_str, " is the reversed number")
        print()
    elif ch == 2:
        str = input("Enter the number: ")
        print()
        new_str = str[::-1]
        if str == new_str:
            print("Yes, it is a palindrome")
            print()
        else:
            print("It is not a palindrome")
            print()
    else:
        print("Goodbye!")
        break
