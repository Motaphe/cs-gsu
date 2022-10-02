## Prolog
# Author: Suzal Regmi
# Email: sregmi2@student.gsu.edu
# Section: 036
# Timestamp: 12:48 pm, September 13

'''
Purpose: 
Calculation of Compound Interest 

Pre-Conditions (input):
The principal amount
The annual interest rate
The number of times interest is applied per year
The number of years interest is applied for

Post-Conditions (output):
The equivalent Compound Interest
'''

# The Design:

# Import the 'pow' function from the 'math' library.
from math import pow

# Define the main function which will store most of the code.
def main(): 
    
    # Display the introductory message.
    print ("\n       *** Compound Interest ***\n")
    
    # Ask the user for all necessary inputs.
    principal = float(input("What is the principal amount? ($) "))
    rate = float(input("What is the annual interest rate? (%) "))
    number_of_times = int(input("What is the number of times per year is the interest applied? "))
    time_in_years = float(input("What is the number of years interest applied? "))

    # Calculate the Compound Interest using it's formula.
    compound_interest = (principal*(pow(1+rate/(number_of_times*100),number_of_times*time_in_years)))

    # Print code according to what is specified.
    print (f"\nThe total amount accrued, principal plus interest, with compound interest on " \
        f"a principal ${principal:.2f} at a rate of {(str(rate)).rstrip('.0')}% per year compounded {(str(number_of_times)).rstrip('.0')} times per year " \
        f"over {(str(time_in_years)).rstrip('.0')} years is ${compound_interest:.2f}.\n")


# Call the main function.
if __name__ == "__main__":
    main()


'''
Test Case 1:

       *** Compound Interest ***

What is the principal amount? ($) 2500.00
What is the annual interest rate? (%) 6.0
What is the number of times per year is the interest applied? 12
What is the number of years interest applied? 2

The total amount accrued, principal plus interest, with compound interest on 
a principal $2500.00 at a rate of 6% per year compounded 12 times per year 
over 2 years is $2817.90.


Test Case 2:

       *** Compound Interest ***

What is the principal amount? ($) 15500.00
What is the annual interest rate? (%) 4.5
What is the number of times per year is the interest applied? 6
What is the number of years interest applied? 4

The total amount accrued, principal plus interest, with compound interest on 
a principal $15500.00 at a rate of 4.5% per year compounded 6 times per year 
over 4 years is $18544.41.


Test Case 3:

       *** Compound Interest ***

What is the principal amount? ($) 10000
What is the annual interest rate? (%) 3.65
What is the number of times per year is the interest applied? 12
What is the number of years interest applied? 7.5

The total amount accrued, principal plus interest, with compound interest on 
a principal $10000.00 at a rate of 3.65% per year compounded 12 times per year 
over 7.5 years is $13143.40.


Test Case 4:

       *** Compound Interest ***

What is the principal amount? ($) 5080
What is the annual interest rate? (%) 4.95
What is the number of times per year is the interest applied? 365
What is the number of years interest applied? 3

The total amount accrued, principal plus interest, with compound interest on 
a principal $5080.00 at a rate of 4.95% per year compounded 365 times per year 
over 3 years is $5893.21.


Test Case 5:

       *** Compound Interest ***

What is the principal amount? ($) 45000
What is the annual interest rate? (%) 9
What is the number of times per year is the interest applied? 1
What is the number of years interest applied? 4

The total amount accrued, principal plus interest, with compound interest on 
a principal $45000.00 at a rate of 9% per year compounded 1 times per year 
over 4 years is $63521.17.

'''