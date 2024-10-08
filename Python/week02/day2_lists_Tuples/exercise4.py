# Write a Python program to remove all the duplicates in the list
# list2 = [23, 45, 67, -10, 23, 50 , -10]

list2 = [23, 45, 67, -10, 23, 50 , -10] #create a list list1 containing seven numbers with a duplicate amidst
newList2 = [] #create an empty list to copy items into excluding duplicates

#use a for loop to get every item in list2 and then use not in conditional to skip duplicate numbers
for everyNumber in list2: #create variable everyNumber to get items in list1 sequencially
    if everyNumber not in newList2: #check whether number is absent in the new list
        newList2.append(everyNumber) #append number if it is absent 

print(f"Original list2 with duplicate numbers: {list2}")
print(f"Modified list2 excluding duplicates  : {newList2}")

