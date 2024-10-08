# Write a program that creates a list of numbers or words and then sorts the list in 
# ascending or descending order using built-in functions like sort() or the sorted() method

fruits = ['Mango', 'Banana', 'Apple', 'Quava', 'Pineapple'] # create a list of fruits
numbers = [17, 5, 29, 7, 3, 11, 13, 2, 19, 23] # create a list of numbers and store them in a list called numbers

print(f"Original fruits list: {fruits}")
print(f"Sorted fruits list:   {sorted(fruits)} \n") #use sorted function to arrange items in fruits list alphabetically without modifying the fruits list

print(f"original numbers list: {numbers}")
numbers.sort() #use sort function to arrange items in numbers from smallest and replace numbers list
print(f"sorted numbers list:   {numbers}")
