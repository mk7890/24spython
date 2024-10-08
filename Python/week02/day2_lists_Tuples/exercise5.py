# Write a program that creates a list of numbers and then iterates through the list
# using a for loop, printing each element and its index

myListOfNUmbers = [10 ,20, 30, 40, 50] #create a list called myListOfNumbers
for myElement in myListOfNUmbers:   #create a for loop to get every item in the list 
    index = myListOfNUmbers.index(myElement) #use index built in function to get the index of every element in the list
    print(f"Element {myElement}  index {index}") #print element and its index in the list