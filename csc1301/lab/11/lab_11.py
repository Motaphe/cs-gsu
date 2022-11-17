# Prolog
# Author: Suzal Regmi
# Email: sregmi2@student.gsu.edu
# Section: 036
# Timestamp: 11:00 pm, November 11

'''
Purpose: 
- practice reading data from a file and writing data to the file
- practice using random library
- creating functions and saving them in modules
- calling functions and evaluation of return values

Pre-Conditions (input):
Asks the user to enter the amount of numbers to be written to a file

Post-Conditions (output):
- creates a new file test.txt and writes to it a predetermined amount of
random numbers (use the constant sequence created by using
the random.seed() function)
- determines how many of the entered numbers are primes
- writes primes number in the file prime.txt
- displays all numbers in the file
- displays the list of prime numbers
- displays the total quantity of prime numbers
'''

# The Design:

# Import necessary libraries
import random

# Build a function that writes the numbers into a file


def write(how_many):
    with open("test.txt", "w") as file:
        random.seed(2)
        for _ in range(how_many):
            num = random.randint(1, 100)
            file.write(f"{str(num)} ")
            if num > 1:
                write_prime(num)


# Build a function that writes the prime numbers into another file
def write_prime(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False

    if is_prime == True:
        with open("prime.txt", "a") as file:
            file.write(f"{str(num)} ")


# Build a function that prints out the numbers and the prime numbers
def show():
    print("\nThe numbers: ", end="")
    with open("test.txt", "r") as file:
        for _ in file:
            print(_)

    print("\nPrime number/s: ", end="")
    count = 0
    with open("prime.txt", "r") as file:
        for _ in file:
            print(_)
            count += 1

        if count == 1:
            print(f"There was {count} prime number\n")

        else:
            print(f"There were {count} prime numbers\n")


# Build a function which calculates the sum of digits of any number and displays the max
def count():
    max_sum = 0
    max_char = ""
    with open("test.txt", "r") as file:
        for row in file:
            num = row.split()
            for one in num:
                sum = 0
                for i in range(len(one)):
                    sum += int(one[i])
                if sum > max_sum:
                    max_sum = sum
                    max_char = one

    print(f"{max_char} has a maximum sum of digits = {max_sum}\n")


# Build the main function that initializes every other function
def main():
    how_many = int(
        input("Enter the amount of numbers to be written to the file: "))
    write(how_many)
    show()
    count()


# Call the main function only if directly running this particular program.
if __name__ == "__main__":
    main()
