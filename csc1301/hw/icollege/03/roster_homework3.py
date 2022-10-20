## Prolog
# Author: Suzal Regmi
# Email: sregmi2@student.gsu.edu
# Section: 036
# Timestamp: 2:30 pm, October 20

'''
Purpose: 
We are building a roster managment for the Atlanta Braves (World series Champions) and are
allowing the user to 1) lookup a player stats, 2) add a player in the roster
with stats about them 3) remove a player from the roster

Pre-Conditions (input):
What does the user want to do? 1) lookup a player stats, 2) add a player in the roster
with stats about them, or 3) remove a player from the roster.

Post-Conditions (output):
Depending on the user's input, the program processes the request and gives out the output.
'''

## Design

# Import unittest to test our functions
import unittest

# Define a main function
def main():

    # Initialize the roster with data of two players
    brave_roster = {
          'Austin Riley': 'AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273',
          'Ronald Acuna': 'AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266',
          }    

    # Display introductory message
    print("\n           *** Braves Stats ***\n\nWelcome to My Braves Stats! What can i do for you?\n\n1. Search for a player\n2. Add a new player\n3. Remove a player")
    
    # Ask the user what to do
    choice = int(input("\nPlease type your choice number: "))
    while choice < 1 or choice > 3:
        choice = int(input("\nINVALID CHOICE\n\nPlease type your choice number(1, 2, or 3): "))

    # Depending on user input, initialize the relevant function
    if choice == 1:
        lookup_player(brave_roster, who = input("\nEnter the name of the player you want to look up: "))
    elif choice == 2:
        who = input("\nEnter the name of the player you want to add: ").strip()
        try:
            who_stats = input(f"Please add {who[:who.index(' ')]}'s stats: ")
        except (ValueError):
            who_stats = input(f"Please add {who}'s stats: ")
        add_player_to_dict(brave_roster, who, who_stats)
    elif choice == 3:
        delete_in_dict(brave_roster, who = input("\nEnter the name of the player you want to remove: "))

# Define the 3 functions
def lookup_player(brave_roster, who):

    # If the player is in the team, print out their stats
    if who in brave_roster:
        try:
            print (f"\nHere's {who[:who.index(' ')]}\'s stats: {brave_roster[who]}\n\nThanks for using My Braves Stats.\n")
        except (ValueError):
            print (f"\nHere's {who}\'s stats: {brave_roster[who]}\n\nThanks for using My Braves Stats.\n")
        return (brave_roster[who])

    # Else, If the player is not in the team, print an error message
    else:
        print (f"\nuh typo? {who} does not play for us :)\n")
        return ("N/A")

def add_player_to_dict(brave_roster, who, who_stats):

        # If there is already an existing player with the same name as the new player, symbolize the new player as
        # his_name + (number_of_other_players_having_the_same_name + 1)
        if who in brave_roster:
            i = 2
            while True:
                if f"{who}({i})" in brave_roster:
                    i += 1
                else:
                    who = f"{who}(2)"
                    break
        
        # Add the player and their stats to the team
        brave_roster[who] = who_stats

        # Print the new complete team
        print ("\nHere's the complete team roaster: \n")
        for player in brave_roster:
            print (f"   {player}: {brave_roster[player]}")
        print ()
        return brave_roster
    
def delete_in_dict(brave_roster, who):

    # If the player exits in the team, delete them and their stats
    if who in brave_roster:
        del brave_roster[who]
        print (f"\nBye Bye {who}!\n")

    # If the player doesnt exist in the team, print out an error message
    else:
        try:
            print (f"uh typo? {who[:who.index(' ')]} does not play for us")
        except (ValueError):
            print (f"\nuh typo? {who} does not play for us\n")
    return brave_roster

# Unit Tests 
class TestDictFunctions(unittest.TestCase):

  def test_search_player_success(self):
    test_dict = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"
    }
    actual = test_dict["Austin Riley"]
    expected = lookup_player(test_dict, "Austin Riley")
    self.assertEqual(actual, expected)

  def test_search_player_no_result(self):
    test_dict = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"
    }
    actual = "N/A"
    expected = lookup_player(test_dict, "Ronald Acuna")
    self.assertEqual(actual, expected)

  def test_add_player_sucess(self):
    test_dict = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"
    }
    actual = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273",
		"Ronald Acuna": "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266"
    }
    expected = add_player_to_dict(test_dict, "Ronald Acuna", "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266")

    self.assertEqual(actual, expected)

  def test_add_player_duplicate(self):
    test_dict = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"}
    actual = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273", "Austin Riley(2)": "AB: 350, R: 20, H: 120, HR: 5, AVG: 0.214"}
    expected = add_player_to_dict(test_dict, "Austin Riley", "AB: 350, R: 20, H: 120, HR: 5, AVG: 0.214")
    self.assertEqual(actual, expected)

  def test_delete_player_sucess(self):
    test_dict = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"}
    expected = {}
    actual = delete_in_dict(test_dict, "Austin Riley")
    self.assertEqual(actual, expected)

  def test_delete_word_no_result(self):
    test_dict = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"}
    expected = test_dict
    actual = delete_in_dict(test_dict, "Shohei Ohtani")
    self.assertEqual(actual, expected)


unittest.main()

