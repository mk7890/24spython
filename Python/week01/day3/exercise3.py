#Program to check if a number is Prime or not using a While loop

number = int(input("Enter a number to check if it's prime: "))
numberIsPrime = True 

if number < 2:
    print(f"{number} is not a prime number")
while number >=2: 
    for i in range(2, number): 
        if number % i == 0: 
            numberIsPrime = False 
    
    if numberIsPrime == True: 
        print(f"{number} is a prime number") 
    else: 
        print(f"{number} is not a prime number")