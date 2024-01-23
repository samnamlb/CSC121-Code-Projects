#
# Aleem Azimov
# 10/22/2022
# This program stores user-entered data into dictionaries and outputs
# the results.
#
def main():
    # TODO - Create three empty dictionaries named inventory_counts,
    #  inventory_costs, and inventory_descriptions
    inventory_counts = {}
    inventory_costs = {}
    inventory_descriptions = {}

    print("Welcome to Trish's Inventory Input System")
    while True:
        item_name = get_item_name()
        item_count = get_item_count()
        unit_cost = get_unit_cost()
        description = get_description()

        # TODO - Add the item data to the three dictionaries. Use the item_name
        #  as a key for all dictionaries.
        #     - Add the item_count data as a value associated with the key
        #       item_name in inventory_counts.
        #     - Add the unit_cost data as a value associated with the key
        #       item_name in inventory_costs.
        #     - Add the description data as a value associated with the key
        #       item_name in inventory_descriptions.
        inventory_counts[item_name] = item_count
        inventory_costs[item_name] = unit_cost
        inventory_descriptions[item_name] = description

        answer = ''
        while answer != 'y' and answer != 'n':
            answer = input('Enter another item? (y/n) ')
            answer = answer.lower()
            if answer != 'y' and answer != 'n':
                print('Enter y or n to continue.')
        if answer == 'n':
            break

    # TODO - Print the three dictionaries as shown in assignment's
    #  sample output.
    print(f'Inventory counts: {inventory_counts}')
    print(f'Inventory costs: {inventory_costs}')
    print(f'Inventory descriptions: {inventory_descriptions}')


def get_item_name():
    # Get item name
    while True:
        item_name = input('Enter the item name: ')
        if ',' in item_name:
            print('Item names cannot contain commas.')
        else:
            break
    return item_name


def get_item_count():
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
    return item_count


def get_unit_cost():
    # Get unit cost
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except:
            print('Unit cost can only contain digits and a single decimal point.')
    return unit_cost


def get_description():
    # Get description
    while True:
        description = input('Enter the description: ')
        if ',' in description:
            print('Descriptions cannot contain commas.')
        else:
            break
    return description


main()
