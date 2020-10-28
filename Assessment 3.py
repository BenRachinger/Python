#Author : Ben Rachinger
#Date   : 01/09/2020
#Version: 1.5
################################################
#Maths Quest

#Prints Welcome to Maths Quest
print("Welcome to Maths Quest!")
#Asks for the user to input their name
name = input("What is your name? ")

#Sets a value for a while loop.
practice = "y"
#Sets a while loops conditions.
while practice == "y":
    #Ask the user what times table they would like to practice. The int ensures the program input is a integer.
    TimesTable=int(input("Hi " + name + ", which times table would you like to practice? (1-12): "))
    #Create an IF statement to print an error if value is NOT between 1 and 12, then repeat the loop
    if TimesTable < 0 or TimesTable == 0 or TimesTable > 12:
        print("This input is invalid, Please try again. (1 - 12)")
        
    else:
        practice = "n"     
        print("Ok " + name + ": on a piece of paper, write down the " + str(TimesTable) + " times table from 1 to 12.  When you’re ready I’ll show you the answer so you can check your work.")
        
        
ready = "y"
while ready == "y":
    #Ask for user input. The .lower() at the end of the code line makes all input lowercase to ensure Y or N are acceptable inputs.
    isReady = input("Are you ready? (Enter 'y' to start) ").lower()
    #If the unput is neither y or n, print the input invalid message.
    if isReady != "y" and isReady != "n" :
            print ("This input is invalid, please try again!")
    if isReady == "y":
        ready="n"
        print("\n")
            
        for num1 in range(TimesTable,(TimesTable+1)):
            for num2 in range (1,13):
                print(num2,"x",num1,"=",num2*num1)

#Creates a new variable and while loop about whether the user got their times table correct or not.
answer="y"
while answer=="y":
        correct=input("Did you get them all correct? (y/n): ").lower()
        if correct != "y" and correct != "n" :
            print ("This input is invalid, please try again!")
        if correct=="n":
            print("Better luck next time!")
            exit()
        if correct=="y":
            print("Great Job! Thank you for playing Math Quest!")
            exit()