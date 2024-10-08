#Palindrome checking program

myString = input("Enter a string to check for Palindrome: ") #prompt user to enter a string
#use the double full colon function to reverse captured string and compare it to its original
if myString==myString[::-1]: #if reversed string characters are the same, code below executes
    print(f"{myString} is a Palindrome")
else: #code below executes when reversed characters don't match normal non-reversed word characters
    print(f"{myString} is not a Palindrome")