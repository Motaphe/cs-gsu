## Prolog
# Author: Suzal Regmi
# Email: sregmi2@student.gsu.edu
# Section: 036
# Timestamp: 09:20 pm, October 14

'''
Purpose: 
To do some particular computations

Pre-Conditions (input):
Numbers for particular computations.

Post-Conditions (output):
List of numbers depending on the particular computation.
'''

## The Design:

# Define the function that makes a list starting from 0
# to the particular number, but doesnt include the number. 
def makelist(num):
    return [i for i in range(num)]

# Define the function that does a countdown starting from the particular
# number to 1 and then displays the launch off message.
def rocketcountdown(num):
    lst = [i for i in range(num, 0, -1)]
    lst.append("We have lift off!")
    return lst

# Define the function that takes two numbers as inputs and returns
# the relevant list as output.
def doubleloop(num1, num2):
    return [f"{i}:{j}" for i in range(num1) for j in range(num2)]

# Define the main function to text the other functions    
def main():
    print (makelist(10))
    print (makelist(3))

    print (rocketcountdown(10))
    print (rocketcountdown(2))

    print (doubleloop(3, 3))
    print (doubleloop(3, 4))

# Call the main function only if directly running this particular program.
if __name__ == "__main__":
    main()