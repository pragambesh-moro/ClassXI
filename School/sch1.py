#Program to find area/circ
import math as m
while True:
    print("Menu: ")
    print("1. Find the area")
    print("2. find the circumfrence")
    print("3. Exit")
    ch = int(input("Enter Choice: "))
    if ch == 1:
        r=int(input("Enter Radius: "))
        area = m.pi*m.pow(r, 2)
        print(area, " is the area")
    elif ch == 2:
        r=int(input("Enter Radius: "))
        circ = 2*m.pi*r
        print(circ, " is the circumfrence")
    else:
        print("Goodbye!")
        break