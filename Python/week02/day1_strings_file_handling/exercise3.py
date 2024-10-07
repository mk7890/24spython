#Palindrome checking program

myString = input("Enter a string to check for Palindrome: ") #prompt user to enter a string

if myString==myString[::-1]: #use the double full colon function to reverse captured string and compare it to its original
    print(f"{myString} is a Palindrome")
else:
    print(f"{myString} is not a Palindrome")