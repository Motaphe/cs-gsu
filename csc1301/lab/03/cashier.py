## Prolog
# Author: Suzal Regmi
# Email: sregmi2@student.gsu.edu
# Section: 036
# Timestamp: 12:19
'''
Purpose: 
calculate the change you are due when you buy an item in a store
Pre-conditions (input): 
money given to the cashier(cost of item)
Post-conditions (output): 
change user get back from the cashier(dollars, quarters, dimes, nickels and 
pennies)
'''
def main():
    # Design and implementation
    # 1. Output a message to identify the program, and a blank line
    print()
    print("Conversion of change to dollars, quarters, dimes, nickels and pennies")
    # 2. Input amount of change from user
    amt = float(input("Enter the change amount: "))
    # 3. Calculate the change to dollars, quarters, dimes, nickels and pennies
    dollars = int(amt)
    quarters = int(((amt-dollars)*100)/25)
    dimes = int(((amt-dollars)*100-(quarters*25))/10)
    nickels = int(((amt-dollars)*100-(quarters*25)-(dimes*10))/5)
    pennies = int((amt-dollars)*100-(quarters*25)-(dimes*10)-(nickels*5)) 
    # 4. Output resulting change 
    print()
    print("You will get;")
    print("Dollars: ", dollars)
    print("Quarters: ", quarters)
    print("Dimes: ", dimes)
    print("Nickels: ", nickels)
    print("Pennies: ", pennies)
main()
# end of program file

"""
Errors and Fixes:
1) Syntax Error - Line 24
TypeError: unsupported operand type(s) for -: 'str' and 'int'
We are trying to perform a mathematical computation between a string and an interger.
Adding a float converter to the amt input (line 21), resolves the issue.  

2) Semantics Error - Line 24
Although the syntax is now correct, there is a flaw in the logic of the mathematical computation
that is resulting in incorrect output. To calculate quaters, we need to multiply the 
subtraction between amt and dollars by 100 and not add 100. So replacing the "+" with a "*" resolved the issue.

Test Cases:
1) Conversion of change to dollars, quarters, dimes, nickels and pennies
Enter the change amount: 1.57

You will get;
Dollars:  1
Quarters:  2
Dimes:  0
Nickels:  1
Pennies:  2

2) Conversion of change to dollars, quarters, dimes, nickels and pennies
Enter the change amount: 2.56

You will get;
Dollars:  2
Quarters:  2
Dimes:  0
Nickels:  1
Pennies:  1

3) Conversion of change to dollars, quarters, dimes, nickels and pennies
Enter the change amount: 0

You will get;
Dollars:  0
Quarters:  0
Dimes:  0
Nickels:  0
Pennies:  0
"""