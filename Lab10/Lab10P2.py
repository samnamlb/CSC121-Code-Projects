#
# Aleem Azimov
# 10/28/22
# Trish's Bookstore Inventory System
#
import pickle


# Review the main() function and update TODO sections.
# Do not change any other code within main().
def main():
    inventory_counts, inventory_costs, inventory_descriptions = read_inventory_file()

    print("Welcome to Trish's Inventory Input System")
    print("Current Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_descriptions)

    response = ''
    while response != '0':
        # Display the user menu
        print("What would you like to do?")
        print("(1) Add an item\n"
              "(2) Display an item\n"
              "(3) Delete an item\n"
              "(4) Display all inventory\n"
              "(0) Exit")

        response = input('Enter your choice: ')
        if response == "1":  # Add an item
            item_name, item_count, unit_cost, description = get_item_input()
            # TODO - Replace pass with code that will add the item_name,
            #  item_count, and unit_cost data to the dictionaries
            inventory_counts[item_name] = item_count
            inventory_costs[item_name] = unit_cost
            inventory_descriptions[item_name] = description
            print(f'{item_name} added to inventory.\n')
        elif response == "2":  # Display an item
            item_name = input('Enter item name: ')
            # TODO - Replace pass with code that will display the item data
            #  from the dictionaries or display "Not found"
            if item_name in inventory_counts:
                print(item_name)
                print(f'\tCount: {inventory_counts[item_name]}, Cost: {inventory_costs[item_name]}')
                print(f'\t{inventory_descriptions[item_name]}')
            else:
                print(f'{item_name}: Not found')
            print('')
        elif response == "3":  # Delete an item
            item_name = input('Enter item name: ')
            # TODO - Replace pass with code that will remove the item data
            #  from the dictionaries or display "Not found"
            if item_name in inventory_counts:
                del inventory_counts[item_name]
                del inventory_costs[item_name]
                del inventory_descriptions[item_name]
                print(f'{item_name} deleted.')
            else:
                print(f'{item_name}: Not found')
            print('')
        elif response == "4":  # Display all inventory
            # TODO - Replace pass with code that will display all the inventory
            #  items - HINT Don't we already have a function that does that?
            display_all_inventory(inventory_counts, inventory_costs, inventory_descriptions)
        elif response != "0":
            print("Invalid choice. Try again.\n")

    # Ready to exit the program, display and save inventory as last steps
    print("Final Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_descriptions)

    save_inventory_file(inventory_counts, inventory_costs, inventory_descriptions)


def display_all_inventory(inventory_counts, inventory_costs, inventory_descriptions):
    # TODO - Replace pass with code that will iterate through the dictionaries
    #  that are passed in and display the inventory. If the dictionaries are
    #  empty the display "== Empty =="
    print(f'Item name      Count   Unit Cost  Description')
    print(f'---------      -----   ---------  -----------')
    if len(inventory_counts) > 0:
        for k in inventory_counts:
            print(f'{k:<15}{inventory_counts[k]:^9}{inventory_costs[k]:>8.2f}  {inventory_descriptions[k]}')
    else:
        print('== Empty ==')
    print('')


def save_inventory_file(inventory_counts, inventory_costs, inventory_descriptions):
    # TODO - Replace pass with code that will save your dictionaries to
    #  inventory.dat using the pickle module.
    inventory = open('inventory.dat', 'wb')
    pickle.dump(inventory_counts, inventory)
    pickle.dump(inventory_costs, inventory)
    pickle.dump(inventory_descriptions, inventory)
    inventory.close()
    print('Inventory.dat file was created.')


def read_inventory_file():
    # TODO - Replace pass with code that will read your dictionaries from
    #  inventory.dat using the pickle module.
    try:
        inventory = open('inventory.dat', 'rb')
        inventory_counts = pickle.load(inventory)
        inventory_costs = pickle.load(inventory)
        inventory_descriptions = pickle.load(inventory)
    except FileNotFoundError:
        inventory_counts = {}
        inventory_costs = {}
        inventory_descriptions = {}
    return inventory_counts, inventory_costs, inventory_descriptions


# This function is complete, no changes needed, but feel free to review
def get_item_input():
    # Get item name
    while True:
        item_name = input('Enter the item name: ')
        if ',' in item_name:
            print('Item names cannot contain commas.')
        else:
            break
    # Get item count
    while True:
        try:
            item_count = int(input('Enter the item count: '))
            if item_count < 0:
                print('Item count must be 0 or greater.')
            else:
                break
        except:
            print('Item count must be an integer.')
    # Get unit cost
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except:
            print('Unit cost must be an integer.')
    # Get description
    while True:
        description = input('Enter the description: ')
        if ',' in description:
            print('Descriptions cannot contain commas.')
        else:
            break
    return item_name, item_count, unit_cost, description


main()
