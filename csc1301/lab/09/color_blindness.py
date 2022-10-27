## Prolog
# Author: Suzal Regmi
# Email: sregmi2@student.gsu.edu
# Section: 036
# Timestamp: 1:20 pm, October 27

'''
Purpose: 
To test what colors affect which type of color blindness

Pre-Conditions (input):
The choice of whether to view pre existing test reults or test new colors and subsequently
the hexadecminal equivalent of a color

Post-Conditions (output):
Result of Test Cases or Result of the Color which was passed during Input
'''

## The Design:

# Extract the red component from the string and return its equivalent decimal value
def get_red(color):
    return int(color[0:2], 16)

# Extract the green component from the string and return its equivalent decimal value
def get_green(color):
    return int(color[2:4], 16)

# Extract the blue component from the string and return its equivalent decimal value
def get_blue(color):
    return int(color[4:6], 16)

# Check if the colour affects Protanopia
def id_protanopia(color):
    check_for_red = get_red(color)
    if check_for_red < 64:
        return True
    else:
        return False

# Check if the colour affects Deuteranopia
def id_deuteranopia(color):
    check_for_green = get_green(color)
    if check_for_green < 64:
        return True
    else:
        return False

# Check if the colour affects Tritanopia
def id_tritanopia(color):
    check_for_red = get_red(color)
    check_for_green = get_green(color)
    check_for_blue = get_blue(color)

    if check_for_blue > 0 and check_for_red > 230 and check_for_green > 220:
        return False
    else:
        return True

# Implement a function for pre existing tests
def run_tests():
    print (f"Should print 37: {get_red('2596be')}")  
    print (f"Should print 235: {get_red('eb4034')}") 

    print (f"Should print 98: {get_green('4d6285')}")
    print (f"Should print 12: {get_green('170c0b')}")

    print (f"Should print 152: {get_blue('42f598')}")  
    print (f"Should print 14: {get_blue('1a0f0e')}")

    print (f"Should print True: {id_protanopia('2596be')}") 
    print (f"Should print False: {id_protanopia('692924')}")
    print (f"Should print True: {id_protanopia('3c2924')}")
    
    print (f"Should print False: {id_deuteranopia('384035')}")
    print (f"Should print True: {id_deuteranopia('333b31')}")

    print (f"Should print False: {id_tritanopia('eeeee4')}")
    print (f"Should print True: {id_tritanopia('000301')}")

# Implement a function that checks a colour for all color blindness
def run_custom_test(color):
    print (f"\nRed: {int(color[0:2], 16)}")
    print (f"Green: {int(color[2:4], 16)}")
    print (f"Blue: {int(color[4:6], 16)}\n")

    if int(color[0:2], 16) < 64:
        print ("This color affects Protanopia")
    else:
        print ("This color doesnt affect Protanopia")
    
    if int(color[2:4], 16) < 64:
        print ("This color affects Deuteranopia")
    else:
        print ("This color doesnt affect Deuteranopia")

    if int(color[4:6], 16) > 0 and int(color[0:2], 16) > 230 and int(color[2:4], 16) > 220:
        print ("This color affects Tritanopia\n")
    else:
        print ("This color doesnt affect Tritanopia\n")

# Define the main function
def main():
    choice = int(input("Do you want to\n 1) View pre exiting test results. \n 2) Test new colors \n Choice: "))
    if choice == 2:
        run_custom_test(input("The hexadecminal equivalent of a color: "))
    else:
        run_tests()
            
# Call the main function only if directly running this particular program.
if __name__ == "__main__":
    main()