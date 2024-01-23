#
# Aleem Azimov
# 11/5/2022
# Classes and OO Programming - Problem 2
#
import pickle
from inventory_item import InventoryItem


def main():
    inventory = load_inventory()
    display_inventory(inventory)

    answer = ''
    while answer.lower() != 'n':
        # TODO - Create an InventoryItem object, ask the user for item input
        #  using the object's method, then append the object to the inventory
        #  list.
        item = InventoryItem()
        item.get_item_input()
        inventory.append(item)
        answer = input('Do you want to enter more items? ')

    display_inventory(inventory)
    save_inventory(inventory)


def load_inventory():
    inventory = []
    # TODO - Attempt to load inventory data from a binary file named
    #  inventory.dat. If the file exists, load it into the inventory list.
    #  If the file does not exist, leave the inventory list empty.
    try:
        files = open('inventory.dat', 'rb')
        inventory = pickle.load(files)
        files.close()
    except FileNotFoundError:
        pass
    return inventory


def save_inventory(inventory):
    # TODO - Open a binary file named inventory.dat and dump the inventory
    #  list that has been passed in as a parameter to that file.
    files = open('inventory.dat', 'wb')
    pickle.dump(inventory, files)
    files.close()
    print('Inventory.dat file was created.')


def display_inventory(inventory):
    print()
    print('Current Inventory')
    print('-----------------')
    # TODO - Display the inventory items that are in the inventory list
    #  that was passed in as a parameter. If the list is empty, display
    #  "Inventory is empty."
    if len(inventory) != 0:
        item_str = ''
        for item in inventory:
            item_str += str(item) + '\n'
        print(item_str)
    else:
        print('Inventory is empty.')
    print('-----------------')


main()
