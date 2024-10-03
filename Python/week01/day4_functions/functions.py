# for loop to calculate the sum of numbers from 1 up to a specified number

def sumFunction():
    startNumber = int(input("Enter the starting number: "))
    lastNumber = int(input("Enter your last number: "))
    sum = 0
    for i in range(startNumber, lastNumber):
        sum += i
    return (f"The sum of the numbers {startNumber} to {lastNumber} is = {sum}")

print(sumFunction())