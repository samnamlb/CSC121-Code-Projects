#
# Aleem Azimov
# August 27, 2022
# Dice to Colors
#

# This will be filled in with what we output
# to the user.
outputStr = ''

# Get the dice numbers from the user.
die1 = int(input('Enter the number on the first die (1-6): '))
die2 = int(input('Enter the number on the second die (1-6): '))

# Determine if the die numbers are valid.
if die1 > 6 or die1 < 1:  # Check if die1 is out of range
    outputStr = 'Error - Die 1 number is invalid'
elif die2 > 6 or die2 < 1:  # Check if die2 is out of range
    outputStr = 'Error - Die 2 number is invalid'

# Dice are in the correct range.
# Determine the board color for the roll.
else:
    # When both dice are equal, the color is Blue.
    if die1 == die2:
        outputStr = 'Blue'

    # When both die are even, the color is Green
    elif die1 % 2 == 0 and die2 % 2 == 0:
        outputStr = 'Green'

    # When both die are odd, the color is Yellow
    elif die1 % 2 != 0 and die2 % 2 != 0:
        outputStr = 'Yellow'

    # Not doubles, and dice are not both even or odd,
    # the color is Red
    else:
        outputStr = 'Red'

print(f'Move your token to this color: {outputStr}')
