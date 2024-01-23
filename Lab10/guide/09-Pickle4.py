# Examples of serializing objects with the pickle module
import pickle


def main():
    car_year, car_price = read_inventory()

    display_inventory(car_year, car_price)

    response = ''
    while response.lower() != 'q':
        display_menu()
        response = input('\nWhat do you want to do? (a/u/d/s/q) ')
        if response.lower() == 'a':
            add_car(car_year, car_price)
        elif response.lower() == 'u':
            print('Update - To be implemented')
        elif response.lower() == 'd':
            print('Delete - To be implemented')
        elif response.lower() == 's':
            display_inventory(car_year, car_price)
        elif response.lower() != 'q':
            print('Invalid choice. Try again.')

    print('\nWriting inventory to inventory.dat...')
    write_inventory(car_year, car_price)
    print('Inventory file created.')


def read_inventory():
    """
    This function reads car inventory data from the file inventory.dat and
    returns that data in two dictionaries. If the file is not present, the
    inventory is assumed empty and empty dictionaries are returned.

    :return: tuple with car_year and car_type dictionaries
    """
    try:
        inventory = open('inventory.dat', 'rb')
        car_year = pickle.load(inventory)
        car_price = pickle.load(inventory)
    except FileNotFoundError:
        car_year = {}
        car_price = {}
    return car_year, car_price


def write_inventory(car_year, car_price):
    """

    :param car_year: Dictionary with car name as key and year as value
    :param car_price: Dictionary with car name as key and price as value
    """
    inventory = open('inventory.dat', 'wb')
    pickle.dump(car_year, inventory)
    pickle.dump(car_price, inventory)
    inventory.close()


def add_car(car_year, car_price):
    """
    This function asks the user for car information and adds it to the car
    inventory.

    :param car_year: Dictionary with car name as key and year as value
    :param car_price: Dictionary with car name as key and price as value
    """
    name = input('Enter name of car: ')
    year = int(input('Enter year of car: '))
    price = float(input('Enter price of car: '))
    car_year[name] = year
    car_price[name] = price


def display_inventory(car_year, car_price):
    """
    Displays the car inventory to the user. If the dictionaries are empty
    the program indicates the inventory is empty.

    :param car_year: Dictionary with car name as key and year as value
    :param car_price: Dictionary with car name as key and price as value
    """
    print("Current Inventory")
    print("-----------------")
    if len(car_year) > 0:
        for k in car_year:
            print(f'{k}, Year: {car_year[k]}, Price: {car_price[k]}')
    else:
        print('== Empty ==')
    print()  # Blank line for nicer output


def display_menu():
    """
    Displays the menu of options to the user.
    """
    print('Menu')
    print('----')
    print('a - Add a new car')
    print('u - Update an existing car')
    print('d - Delete a car')
    print('s - Show the current inventory')
    print('q - Save the inventory and quit the program')

main()
