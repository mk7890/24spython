# Write a python program to sum all numbers in the list
# list1 = [10, 20, 30, 40, 50]

list1 = [10, 20, 30, 40, 50] #create a list list1 containing five numbers

# use a for loop to iterate through each item in the list and sum all the numbers
totalSum = 0 #create a variable to hold the sum
for everyNumber in list1: #create a variable everyNumber to iterate through the list1
    totalSum = totalSum + everyNumber #add the value of everyNumber to totalSum in every iteration

#use a formated string to output the total sum of all numbers in the list list1
print(f"The Sum of all numbers in {list1} is : {totalSum}")