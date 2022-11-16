# Importing module for random number generation.
import random

# Range of the values of a dice.
min_val = 1
max_val = 6

# To loop the rolling through user input.
roll_again = "yes"

# Loop.
while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are: ")
    # Generating and printing 1st random integer from 1 to 6.
    print(random.randint(min_val, max_val))
    # Generating and printing 2nd random integer from 1 to 6.
    print(random.randint(min_val, max_val))

    # Asking user to roll the dice again.
    # Any input other than "yes" or "y" will terminate the loop.
    roll_again = input("Roll the dices again (y/N): ")