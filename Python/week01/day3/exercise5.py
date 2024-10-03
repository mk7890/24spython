# for loop to calculate the sum of numbers from 1 up to a specified number

num = int(input("Enter your number: "))
sum = 0
for i in range(1, num):
    sum += i
print(f"The sum of the numbers 1 to {num} is = {sum}")
