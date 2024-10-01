# this program prompts the user to input a number, then finds the square root and print it
import math # import the math library. it contains useful maths related functions such as square root
my_number = input("Enter a number: ") # prompt the user to enter a number and store it to the variable my_number
my_number = int(my_number) # converts my_number to an integer and assigns it to my_number
square_root = math.sqrt(my_number) # use math function to find square root and assign the value to square_root variable
print(f"the square root of {my_number} is {square_root}") # print the square root on the terminal, using formatted string
