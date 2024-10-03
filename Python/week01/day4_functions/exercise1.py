# this program checks whether a number entered by a user is negative or positive
 
def NumberCheck(a):   # create a function with an if else condition
    if a > 0:   # Check if the number is positive  
        print("Your Number is Positive")    
    elif a < 0:   # Check if the number is negative  
        print("Your Number is Negative")     
    else:    # Else the number is zero
        print("Your Number is zero")  
 
a = float(input("Enter a number: "))  # prompt the user to input a number

NumberCheck(a)  #print the result