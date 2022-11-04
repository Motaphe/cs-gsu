## Prolog
# Author: Suzal Regmi
# Email: sregmi2@student.gsu.edu
# Section: 036
# Timestamp: 12:40 pm, November 04

'''
Purpose: 
Implement the Rock Paper Scissors Game

Pre-Conditions (input):
Ask the user to enter a number. The program should decide
whether the number is to be assigned to Rock or Paper or Scissors and inform the user.

Post-Conditions (output):
The result of the game including both the user and computer choice.
'''

## The Design:

# Import necessary libraries
import sys
import random

def main():
    # Print the title ”The Rock Paper Scissors Game”.
    print ("\nThe Rock Paper Scissors Game\n")

    # Set the variable rock to be 1, the variable paper to be 2 and the variable scissors to be 3.
    rock = 1
    paper = 2
    scissors = 3

    # Set the user’s input to be 0.
    user = 0    

    # Ask to user to enter 1 to choose rock, 2 to choose paper, 3 to choose scissors or -1 to quit the game.
    user = int(input("Please enter 1 for rock, 2 for paper,\n3 for scissors or -1 to quit: "))

    # While the user has not entered -1:
    while user != -1:
        # Randomly assign rock, paper or scissors as the computer’s choice by generating a random number between 1 and 3 and assigning it to a variable named computer choice.
        computer_choice = random.randint(1,3)
        
        # Print what the user chose
        if user == 1:
            print ("\nYou chose rock")
        elif user == 2:
            print ("\nYou chose paper")
        elif user == 3:
            print ("\nYou chose scissors")
        
        # Print what the computer chose
        if computer_choice == 1:
            print ("The computer chose rock\n")
        elif computer_choice == 2:
            print ("The computer chose paper\n")
        elif computer_choice == 3:
            print ("The computer chose scissors\n")
        
        # Print the results of the game
        if user == 1:
            if computer_choice == 2:
                print ("Sorry you lose!")
            elif computer_choice == 3:
                print ("Congratulations you win!")
            else:
                print ("The match was a tie")
        
        elif user == 2:
            if computer_choice == 1:
                print ("Congratulations you win!")
            elif computer_choice == 3:
                print ("Sorry you lose!")
            else:
                print ("The match was a tie")
            
        elif user == 3:
            if computer_choice == 1:
                print ("Sorry you lose!")
            elif computer_choice == 2:
                print ("Congratulations you win!")
            else:
                print ("The match was a tie")

        # Print Goodbye
        sys.exit("\nGoodbye\n")

    # Print Goodbye
    sys.exit("\nGoodbye\n")

# Call the main function only if directly running this particular program.
if __name__ == "__main__":
    main()








