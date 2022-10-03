"""
Modify the guessing-game program below so that the user thinks of a number
that the computer must guess. The computer must make no more than
the minimum number of guesses, and it must prevent the user from cheating
by entering misleading hints.

(Hint: Use the math.log function to compute the minimum number of guesses
needed after the lower and upper bounds are entered.)

"""

import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
what_to_guess = int(input("Enter the number to be guessed: "))
minimum_tries = int(input("How many tries do you want to give the computer?: "))
count = 0

while minimum_tries != 0:
    count += 1
    userNumber = int(random.randint(smaller, larger))
    check = input(f"Is is the number {userNumber} ?(<,=,>): ")
    if what_to_guess == userNumber :
        if check == "=":
            print ("YaY!")
            print (f"Only took me {count} tries to get the answer.")
            break
        else:
            print ("CHEATING ALERT!!")

    elif what_to_guess < userNumber:    
        if check == "<":
            larger = userNumber - 1
        else:
            print ("CHEATING ALERT!!")

    elif  what_to_guess > userNumber:
        if check == ">":
            smaller = userNumber + 1
        else:
            print ("CHEATING ALERT!!")

    minimum_tries -= 1
    
if minimum_tries == 0:
    print ("Dang it! I failed to guess the number in time :(")