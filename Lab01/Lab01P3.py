#
# Aleem Azimov
# August 24, 2022
# This program converts a user-entered number of feet and
# converts it to meters.
#
# Note: The number of feet entered could be a floating point
# number.
#

# Get the number of feet.
feet = float(input("Enter number of feet: "))

# Calculate the meter equivalent.
meters = feet / 3.281

# Display the number of meters.
print(f'That is equal to {meters:.2f} meters.')
