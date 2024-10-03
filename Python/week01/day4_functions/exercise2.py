# Functions to calculate the areas of a Square, Rectangle and Circle

def areaOfSquare():
    squareLength = float(input("Enter the length of the square: "))
    area = squareLength * squareLength
    return area

def areaOfRectangle():
    rectangleLength = float(input("Enter the length of the Rectangle: "))
    rectangleWidth = float(input("Enter the width of the Rectangle: "))
    area = rectangleLength * rectangleWidth
    return area

def areaOfCircle():
    circleRadius = float(input("Enter the Radius of the Circle: "))
    area = (22/7)*circleRadius*circleRadius
    return area

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

