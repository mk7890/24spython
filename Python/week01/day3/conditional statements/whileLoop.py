# while loops execute as long as a predefined condition is met

# n = 10

# while n > 0:
#     print (n)
#     n -=1
# print("DONE")

# symbol = '*'
# n = 20
# while n > 0:
#     print(symbol * n)
#     n -= 1
    
# print('done')

# You have three attempts to guess a secret number from 1 - 10

print("This is a Game to guess a secret number from 1 to 10. You have three attempts ")
secretNumber = 7
guessCount = 0

while guessCount < 3:
    userGuess = int(input("Guess a number from 1 to 10: "))
    guessCount += 1
    if userGuess == secretNumber:
        print("You guessed right!")
        break
    elif guessCount == 3:
        print("Wrong Guess. You've exhausted your guess limits")
        break
    else:
        print("Wrong guess. guess again")
    
