# Write a python code to sum all the items in a dictionary
sum = 0
myDictionary = {'student1':22, 'student2':33, 'student3':44}
for key in myDictionary:
    sum = sum + myDictionary[key]
print(f"The Sum of the values is: {sum}")