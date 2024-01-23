#
# Aleem Azimov
# 10/15/2022
# File write and data validation exercise
#

def main():
    inventory_list = []
    print("Welcome to Trish's Inventory Input System")

    while True:
        # Get validated user input on all item parts
        item_name = get_item_name()
        item_count = get_item_count()
        unit_cost = get_unit_cost()
        description = get_description()

        # Put the item data into a comma separated string
        item_info = item_name + ',' + str(item_count) + ',' + \
                    str(unit_cost) + ',' + description

        # Store the item data string into a list that will be used
        # when saving the data to a text file.
        inventory_list.append(item_info)

        # Ask the user if they want to enter more data.
        # Force them to answer y or n.
        answer = ''
        while answer != 'y' and answer != 'n':
            answer = input('Enter another item? (y/n) ')
            answer = answer.lower()
            if answer != 'y' and answer != 'n':
                print('Enter y or n to continue.')
        if answer == 'n':
            break

    write_inventory_file(inventory_list)


# TODO: Fill in the implementation for get_item_name.
#  The item name is not allowed to have commas. Include data validation
#  that will give the user an error for invalid data and continue to ask the
#  user for data until they provide valid data.
def get_item_name():
    while True:
        item_name = input("Enter the item name: ")
        if "," in item_name:
            print('Item names cannot contain commas.')
        else:
            break
    return item_name


# TODO: Fill in the implementation for get_item_count.
#  The item count must be an integer greater than 0. Include data validation
#  that will give the user an error for invalid data and continue to ask the
#  user for data until they provide valid data.
def get_item_count():
    while True:
        try:
            item_count = int(input("Enter the item count: "))
            if item_count < 0:
                print('Item count must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Item count must be an integer.')
    return item_count


# TODO: Fill in the implementation for get_unit_cost.
#  The unit cost must be a float greater than 0. Include data validation
#  that will give the user an error for invalid data and continue to ask the
#  user for data until they provide valid data.
def get_unit_cost():
    # Get unit cost
    while True:
        try:
            unit_cost = float(input("Enter the unit cost: "))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Unit cost can only contain digits and a single decimal point.')
    return unit_cost


# TODO: Fill in the implementation for get_description.
#  The description is not allowed to have commas. Include data validation
#  that will give the user an error for invalid data and continue to ask the
#  user for data until they provide valid data.
def get_description():
    while True:
        description = input("Enter the description: ")
        if "," in description:
            print('Descriptions cannot contain commas.')
        else:
            break
    return description


# TODO: Fill in the implementation for write_inventory_file.
#  Review the problem specification for details.
def write_inventory_file(inventory_list):
    file = open('inventory.csv', 'w')
    for record in inventory_list:
        file.write(record + '\n')
    file.close()
    print('The file inventory.csv was created.')


main()
