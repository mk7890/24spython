# Simple program that asks a user to gues a number between 1 and 5

luckyGuess = 4
userGuess = int(input("Guess an number between 1 and 5: "))

if userGuess == luckyGuess:
    print("Hurray! your guessed the right number")    
elif userGuess == 1:
    print("your guess is not even close")
elif userGuess == 2:
    print("your guess is sort of close")
elif userGuess == 3:
    print("your guess is very close")
elif userGuess == 5:
    print("your guess is very close but more than the luckynumber")
else:
    print("Invalid Entry")