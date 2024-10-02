#Guess a random number between 1 and 100. You have 10 limited attempts to make a correct guess
import random

randomNumber = random.randint(1, 100)
guessCount = 0
guessLimit = 10
attemptsRemaining = 0

while guessCount < guessLimit:
    
    userGuess = int(input("Guess a number from 1 to 100: "))
    guessCount += 1
    attemptsRemaining = guessLimit - guessCount
    if userGuess == randomNumber:
        print("Correct Guess.")
        break
    elif userGuess < randomNumber:
        print(f"Lower Guess. {attemptsRemaining} attempts remaining.")
    elif userGuess > randomNumber:
        print(f"Higher Guess. {attemptsRemaining} attempts remaining.")
print(f"random number generated was {randomNumber}")        
