# Examples of serializing objects with the pickle module
import pickle


def main():
    car_year, car_price = read_inventory()

    display_inventory(car_year, car_price)

    name, year, price = get_new_car()

    car_year[name] = year
    car_price[name] = price

    print('Writing updated inventory to file...')
    write_inventory(car_year, car_price)
    print('Inventory file created.')


def read_inventory():
    try:
        inventory = open('inventory.dat', 'rb')
        car_year = pickle.load(inventory)
        car_price = pickle.load(inventory)
        inventory.close()
    except FileNotFoundError:
        car_year = {}
        car_price = {}
    return car_year, car_price


def write_inventory(car_year, car_price):
    inventory = open('inventory.dat', 'wb')
    pickle.dump(car_year, inventory)
    pickle.dump(car_price, inventory)
    inventory.close()


def display_inventory(car_year, car_price):
    print('Car Inventory')
    print('-------------')
    for k in car_year:
        print(f'{k}, Year: {car_year[k]}, Price: {car_price[k]}')
    print()


def get_new_car():
    name = input('Enter a car name to add: ')
    year = int(input(f'Enter a car year for {name}: '))
    price = float(input(f'Enter a car price for {name}: '))
    return name, year, price

main()
