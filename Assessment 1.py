#Author : Ben Rachinger
#Date   : 21/07/2020
#Version: 1.0
#
#Guess the random number game
#One player vs. the computer

import random
minGuess = 1
maxGuess = 6

#Ask the user for their name and their guess
name = input("What is your name? ")
print("Hi, " + name + "!")
print("Enter a number between: " , minGuess , " and " , maxGuess)
guess = int(input("What is your guess? "))

#Generate a random number and tell the user if they won or lost
secretNumber = random.randint(minGuess, maxGuess)
if (guess == secretNumber):
    print ("Congratulations, you got it right!")
else:
    print("You lose - the number was ",secretNumber)
        
    print("Thank you for playing Guess the Number.")
