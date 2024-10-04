# this is a program you can use to calculate the area of a Square, Rectangle, or Circle

from exercise2 import areaOfSquare
from exercise2 import areaOfRectangle
from exercise2 import areaOfCircle

print(f"This program can calculate the area of a Square, Rectangle, or Circle")
choice = str(input("Enter s for square; r for rectangle; c for circle "))

if choice == 's':
    print(areaOfSquare())
elif choice == 'r':
    print(areaOfRectangle)
elif choice == 'c':
    print(areaOfCircle())
else:
    print(f"You entered a wrong character")