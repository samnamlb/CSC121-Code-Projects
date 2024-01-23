#
# Aleem Azimov
# August 24, 2022
# This program converts a user-entered number of meters and
# converts it to feet.
#
# Note: The number of meters entered could be a floating point
# number.
#

# Get the number of meters.
meters = float(input("Enter number of meters: "))

# Calculate the meter equivalent.
feet = meters * 3.281

# Display the number of meters.
print(f'That is equal to {feet:.2f} feet.')
