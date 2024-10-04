# Rock Paper Scissors game
# Date: October 4th 2024
# Week 1 Assignment
# Student Name: MOSES MUGAMBI

import random
guess = (['rock', 'paper', 'scissors'])

player1Points = 0
computerPoints = 0
roundsPlayed = 0

def computer():
    computerPlay = random.choice(guess)
    return computerPlay

while roundsPlayed < 5:
    print(f"Round {roundsPlayed+1}")
    player1Play = input("rock  paper  scissors: ")
    computerPlay = computer()
    roundsPlayed += 1
    if player1Play == 'rock' and computerPlay == 'scissors':
        player1Points += 1
        print(f"player1 drew   {player1Play}     computer drew {computerPlay}")
        print(f"Player1 Score: {player1Points}   Computer Score: {computerPoints}")
    elif player1Play == 'rock' and computerPlay == 'paper':
        computerPoints += 1
        print(f"player1 drew   {player1Play}     computer drew {computerPlay}")
        print(f"Player1 Score: {player1Points}   Computer Score: {computerPoints}")
    elif player1Play == 'paper' and computerPlay == 'scissors':
        computerPoints += 1
        print(f"player1 drew   {player1Play}     computer drew {computerPlay}")
        print(f"Player1 Score: {player1Points}   Computer Score: {computerPoints}")
    elif player1Play == 'paper' and computerPlay == 'rock':
        player1Points += 1
        print(f"player1 drew   {player1Play}     computer drew {computerPlay}")
        print(f"Player1 Score: {player1Points}   Computer Score: {computerPoints}")
    elif player1Play == 'scissors' and computerPlay == 'rock':
        computerPoints += 1
        print(f"player1 drew   {player1Play}     computer drew {computerPlay}")
        print(f"Player1 Score: {player1Points}   Computer Score: {computerPoints}")
    elif player1Play == 'scissors' and computerPlay == 'paper':
        player1Points += 1
        print(f"player1 drew   {player1Play}     computer drew {computerPlay}")
        print(f"Player1 Score: {player1Points}   Computer Score: {computerPoints}")
    elif player1Play == computerPlay:
        print(f"Same draw.")
        print(f"player1 drew   {player1Play}     computer drew {computerPlay}")
        print(f"Player1 Score: {player1Points}   Computer Score: {computerPoints}")
    else:
        print(f"You entered an invalid choice")
        
    if roundsPlayed == 3 and player1Points == 2 or computerPoints == 2:
        break
    elif roundsPlayed == 4 and player1Points == 3 or computerPoints == 3:
        break
         
if player1Points > computerPoints:
    print(f"Player 1 WINS!")
elif computerPoints > player1Points:
    print(f"Computer WINS!")
elif computerPoints == player1Points: #incase there is a draw
    print(f"Final Score DRAW!")
