##
# Aleem Azimov
# September 10, 2022
# Dice program, stimulates rolling a number of sides of a dice entered by a user
#
import random


# Main
def main():
    # Ask user for number of dice to roll
    userDice = int(input("How many dice do you want to roll? "))

    # Input validation for userDice between 3 and 12
    while 3 > userDice or userDice > 12:
        print("Enter a number between 3 and 12.")
        userDice = int(input("How many dice do you want to roll? "))

    # Ask user for number of sides of the dice
    userSides = int(input("How many sides do the dice have? "))

    # Input validation for userSides between 4 and 20
    while 4 > userSides or userSides > 20:
        print("Enter a number between 4 and 20.")
        userSides = int(input("How many sides do the dice have? "))

    # Roll the dice
    roll_dice(userDice, userSides)


def roll_dice(num_dice, num_sides):
    # Running total
    total = 0
    # The previous roll number
    lastRoll = 0

    # For loop to iterate number of rolls for dice defined by user
    for i in range(1, (num_dice + 1)):

        # Generates random number between 1 and max number of sides defined by user
        rollNum = random.randint(1, num_sides)

        # If the current roll is the same as the last roll, output that user is on a roll
        if rollNum == lastRoll:
            print(f"Dice {i}: {rollNum} -> On a roll!")
        else:
            print(f"Dice {i}: {rollNum}")

        # The current roll becomes previous roll
        lastRoll = rollNum
        # Add current roll number to running total
        total += rollNum

    # Output total rolls
    print(f"Total: {total}")


# Call main function
main()
