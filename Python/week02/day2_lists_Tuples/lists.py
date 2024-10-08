students = ['Richard', 'Ruth', 'Moses', 'Amos', 'Ezekiel']
numbers = [10, 11, 12]
empty = []

# list operations --> *  +
numbersMultiplied = numbers * 2
combined = numbers + students

# list Slicing
#print(students[0:3]) # print elements from index 0 upto and excluding index 3
students[3:5] = ['jesse', 'cyrill'] # replacing the 3rd and 4th elements in students list
# print(students)

# list methods
#   appending
t = [1, 2, 3]
t.append(4)
#print(t)

#   extending
r = [10, 11, 12]
t.extend(r) 

#   sorting
t.sort()
#print(t)

#   Deleting elements from a list
myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#print(myList)
# myList.pop(3) #using pop to delete
# print(myList)

# print(myList)
# del myList[1]  # using del built-in function. slicing is applicable here
# del myList[1:3]
# print(myList)

#myList.remove('a') # using remove method
# print(myList)


# List Functions
myList2 = [2,3,5,7,11,13,17,19,23,29]
# print(len(myList2)) #   length function --> len(myList)
# print(max(myList2)) # max function to get the largest element in the list
# print(min(myList2)) # min function to find the least element in the list
# print(sum(myList2)) # sum function to add elements in a list
# print(sum(myList2)/len(myList2)) # finding the mean of elements in the list


#write a program to ask the user to enter numbers until a 'done' is entered
#then find the sum, length, and average of all entered numbers

totalValue = 0 # variable to hold the totals
myCount = 0 # variable to hold the number of iterations/length

while(True):
    myNumber = input("Enter a number: ")
    if myNumber == 'done':
        break
    totalValue = totalValue + int(myNumber)
    myCount = myCount+1
sum = totalValue
average = sum/myCount
print(f"You entered {myCount} numbers")
print(f"The sum is {sum}")
print(f"Average is {average}")

