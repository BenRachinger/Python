#Author  : Ben Rachinger
#Date    : 23/07/2020
#Version : 1.0
#
#Rock Paper Scissors game
#Two players


#We start with getting the players names.
print("Welcome to Rock, Paper, Scissors!")
print("Let's Begin . . .")
name1 = input("Player 1: What's your name?")
name2 = input("Player 2: What's your name?\n")

print("Hello " + name1 + " and " + name2)
print(name2 + ": Close your eyes!")


#Each player inputs their choice of Rock, Paper or Scissors so the program can compute the winner.

choice1 = input(name1 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ").lower()
print("Great choice! Now - cover your answer and ask " + name2 + " to choose. \n\n\n" )
choice2 = input(name2 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ").lower()

    #The below derives the winner from all possible choices for each player, or a draw.
if choice1 == choice2:
    print("It's a Draw!")
  
elif choice1 == 'r' and choice2 == 's' :
    print(name1 + " wins!")
  
elif choice1 == 'r' and choice2 == 'p':
    print(name2 + " wins!")
  
elif choice1 == 'p' and choice2 == 'r':
    print(name1 + " wins!")
  
elif choice1 == 'p' and choice2 == 's':
    print(name2 + " wins!")

elif choice1 == 's' and choice2 == 'p':
    print(name1 + " wins!")
  
elif choice1 == "s" and choice2 == 'r':
    print(name2 + " wins!")

#This is for input that isn't compatible. It's here to ensure the users realise they've inputted incorrectly.
   
print("Thanks for playing Rock, Paper, Scissors")