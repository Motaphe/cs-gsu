'''
Program: CS 1301 Lab 07

Author: Suzal Regmi
Description: This program will read a positive integer and express it as
the sum of powers of 2.
'''

def main():
    i_num = int(input("Enter a positive integer: "))
    while i_num > 0:
        n = 0
        two_to_n = 2**n

        while two_to_n < i_num:
            n += 1
            two_to_n *= 2

        while two_to_n > i_num:
            n -= 1
            two_to_n //= 2
        
        i_num -= two_to_n

        print (f"2**{n}", end="")
        if n > 1:
            print (" + ", end="")
    print ()

main()