# Create a tuple to store mathematical operators (+  -  *  /) and write a program
# that allows a user to choose and operator and perform basic operations with 
# two numbers

operatorTuple = ('+', '-', '*', '/')
num1 = input('Enter first number : ')
num2 = input('Enter second number : ')
myOperator = input('Enter operator + - * / : ')

if myOperator == operatorTuple[0]:
    print(f"{num1} + {num2} = {int(num1)+int(num2)}")
elif myOperator == operatorTuple[1]:
    print(f"{num1} - {num2} = {int(num1)-int(num2)}")
elif myOperator == operatorTuple[2]:
    print(f"{num1} * {num2} = {int(num1)*int(num2)}")
elif myOperator == operatorTuple[3]:
    print(f"{num1} / {num2} = {int(num1)/int(num2)}")
else:
    print(f"You entered an invalid operator or number")
