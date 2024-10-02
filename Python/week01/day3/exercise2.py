#Program that allows a user to enter two numbers and operator and perform corresponding calculation

print("This programs takes two numbers and an operator to perform a calculation")

firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the secodn number: "))
operator = input("Enter and operator + - * / : ")

if operator == '+':
    print(f"{firstNumber} + {secondNumber} = {firstNumber + secondNumber}")
elif operator == '-':
    print(f"{firstNumber} - {secondNumber} = {firstNumber - secondNumber}")
elif operator == '*':
    print(f"{firstNumber} * {secondNumber} = {firstNumber * secondNumber}")
elif operator == '/':
    print(f"{firstNumber} / {secondNumber} = {firstNumber / secondNumber}")
else:
    print("you entered an invalid operator")
