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
count = 0
while True:
    count += 1
    userNumber = int(random.randint(smaller, larger))
    check = input(f"Is is the number {userNumber} ?(<,=,>): ")
    if check == "=":
        print ("YaY!")
        print (f"Only took me {count} tries to get the answer.")
        break
    
    if check == "<":
        smaller = userNumber
    if check == ">":
        larger = userNumber
