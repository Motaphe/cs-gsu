# Prolog
# Author:  Suzal Regmi
# Email:  sregmi2@student.gsu.edu
# Section: 036
'''
  Purpose:

  1. familiar with the functions 

  2. calculate the Caffeine levels
 
  Pre-conditions (input): 
       (Enter the begining caffeine level)
  Post-conditions (output): 
      get the cafferine level after 6, 12,and 24 hours 
      
'''



# familiar with "function "
"""
We need totally 3 function in our lab today

1. named PrintHello()   
2. named PrintGoodbye()
3. CaffeineLevels()

""" 
# fuction 1 
def PrintHello():
    print("\nHello!\n") 

# fuction2 
def CaffeineLevels():
        
    caffeine_mg = float(input("what's the level of the caffeine now? "))

    print()

    print(f'Your coffeine leavel now is :{caffeine_mg:.2f} \n')

    print("Ok, here is your caffeine levels: \n")

    print(f'After 6 hours: {caffeine_mg / 2:.2f} mg\n')

    print(f'After 12 hours: {caffeine_mg / 4:.2f} mg\n')

    print(f'After 24 hours: {caffeine_mg / 16:.2f} mg\n')

    print(f'After 30 hours: {caffeine_mg / 32:.2f} mg\n')


# fuction3
def PrintGoodbye():  
    print("Thanks, goodbye\n")   


def main(): 

    PrintHello()
    
    CaffeineLevels()

    PrintGoodbye()

 
main()

'''
Syntax Error: Line 31 - A colon is missing after the user defines a function.
SyntaxError: expected ':'
To fix this, I just inserted the colon ':' after defining the funtion.

Semantics Error: Line 49 - The logic of the program was wrong. The level of caffine seems to decrease by 
the powers of 2, every 6 hours. So instead of diving by 8, we divide it by 16. Cause 24/6 = 4 and 2^4=16
not 8.
To fix this, I replaced 8 with 16.


Test Case 1:

Hello!

what's the level of the caffeine now? 345

Your coffeine leavel now is :345.00 

Ok, here is your caffeine levels: 

After 6 hours: 172.50 mg

After 12 hours: 86.25 mg

After 24 hours: 21.56 mg

After 30 hours: 10.78 mg

Thanks, goodbye


Test Case 2:

Hello!

what's the level of the caffeine now? 100

Your coffeine leavel now is :100.00 

Ok, here is your caffeine levels: 

After 6 hours: 50.00 mg

After 12 hours: 25.00 mg

After 24 hours: 6.25 mg

After 30 hours: 3.12 mg

Thanks, goodbye


Test Case 3:

Hello!

what's the level of the caffeine now? 223.6

Your coffeine leavel now is :223.60 

Ok, here is your caffeine levels: 

After 6 hours: 111.80 mg

After 12 hours: 55.90 mg

After 24 hours: 13.97 mg

After 30 hours: 6.99 mg

Thanks, goodbye
'''