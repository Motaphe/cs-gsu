## Prolog
# Author: Suzal Regmi
# Email: sregmi2@student.gsu.edu
# Section: 036
# Timestamp: 10:00 pm, October 4

'''
Purpose: 
Calculating whether the integer inputted is a prime number or not. 

Pre-Conditions (input):
The integer to check.

Post-Conditions (output):
Whether the input is a prime number, a non prime number, or a negative number.
'''

## The Design:

# Import the 'isprime' function from the 'sympy' library.
from sympy import isprime

# Define the function which will return whether the input is a prime number, a non prime number
# or a negative number.
def isItPrime(num):
    # If the number is less than  0, print that it is a negative number.
    if num < 0:
        print (f"The integer {num} is negative. \n")
    # Else, if the function 'isprime' returns True for the number, print that it is a prime number.
    elif isprime(num) == True:
        print (f"The integer {num} is prime. \n")
    # Else, if all above cases fail, print that it is a non prime number. 
    else:
        print (f"The integer {num} is not prime. \n")

# Define the main function.    
def main():
    # Display the introductory message.
    print ("\n     ***  isPrime  ***     ")
    # Ask the user to input an integer and call the function 'isItPrime' on the number to find the result. 
    isItPrime(int(input("Please provide an integer: ")))

# Call the main function only if directly running this particular program.
if __name__ == "__main__":
    main()



'''
Test Case 1:

     ***  isPrime  ***     
Please provide an integer: 2
The integer 2 is prime. 

Test Case 2:

     ***  isPrime  ***     
Please provide an integer: 6
The integer 6 is not prime. 

Test Case 3:

     ***  isPrime  ***     
Please provide an integer: 657
The integer 657 is not prime. 

Test Case 4:

     ***  isPrime  ***     
Please provide an integer: -1
The integer -1 is negative. 

Test Case 5:

     ***  isPrime  ***     
Please provide an integer: 0
The integer 0 is not prime. 

'''