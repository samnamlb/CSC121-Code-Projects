#
# Aleem Azimov
# September 2, 2022
# Pretty Pattern Generator
#

# Ask the user for the number of rows
rows = int(input("How many rows? "))
# Ask the user for the number of columns
columns = int(input("How many columns? "))

# Iterate over the rows.
for row in range(1, rows + 1):

    # Iterate over the columns.
    for col in range(1, columns + 1):
        if row % 2 == 0 and col % 2 == 0:
            print(' ', end='')
        else:
            print('*', end='')

    # Go to the next row.
    print()
