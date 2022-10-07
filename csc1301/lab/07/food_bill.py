## Prolog
# Author: Suzal Regmi
# Email: sregmi2@student.gsu.edu
# Section: 036
# Timestamp: 12:00 pm, October 5

'''
Purpose: 
To calculate the total bill of a customer in a restaurant. 

Pre-Conditions (input):
The customer's order.

Post-Conditions (output):
Their total bill, one without and one including the tip.
'''

## The Design:

# Define the main function.
def main():
    # Assign the menu to a dictionary
    menu = {
        "grilled cheese sandwich": 7, 
        "serving of nachos": 5, 
        "chicken sandwich": 8, 
        "Hamburger": 8,
        "hot dog": 6,    
    }

    # Initialize the total bill of the customer as 0
    total_price = 0

    # Display the introductory message.
    print ("Welcome to Dairy Queen\nPlease answer each question with y or n")
    # Check with the customer for their order and add relevant prices to their bill.
    for item in menu:
        if input(f"Do you want a {item}? ") == "y":
            total_price += menu[item]
            if item == "Hamburger" and input("Do you want cheese on that? ") == "y": total_price += 2  

    # Print out the total price including the tip.
    print (f"The total for your food is ${total_price}\nThe total with 20% tip is ${total_price*1.2:.2f}\nThank you for your business!") 

# Call the main function only if directly running this particular program.
if __name__ == "__main__":
    main()