# Multiplication table using a for loop

num = int(input("Enter the number you want to multiply: "))
limit = int(input("Enter the number of times to multiply: "))

for i in range(1, limit+1):
    print(f"{num} X {i} = {num*i}")
    