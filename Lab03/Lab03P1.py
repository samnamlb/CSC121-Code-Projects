#
# Aleem Azimov
# September 2, 2022
# Inventory Estimator
#

# Get the starting numbers of paperbacks and hardbacks.
paperbacks = int(input('What is the current number of paperbacks? '))
hardbacks = int(input('What is the current number of hardbacks? '))
print()

# Display the inventory stock table.
for month in range(1, 5):
    paperbacks += 100
    hardbacks += 25
    print(f'Month {month}')
    print(f'\tPaperbacks: {paperbacks}')
    print(f'\t Hardbacks: {hardbacks}')
