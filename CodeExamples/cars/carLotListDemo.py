#
# James Matlock
# Apr 7, 2022
# Example for Lesson 12: This program will extend the example we did in Lesson
# 11 where Car objects (and their derived versions) are stored in a list and
# used in a simple inventory program
#

from car import Car
from gasCar import GasCar
from electricCar import ElectricCar
import pickle

def main():
    inventory = load_cars_from_file()
    display_inventory(inventory)

    response = ''
    while response.lower() != 'n':
        choice = ''
        while choice not in ['1', '2', '3']:
            choice = input('What type of car do you want to add? (1-Gas, 2-Electric, 3-Other) ')
            if choice == '1':
                car = GasCar()
            elif choice == '2':
                car = ElectricCar()
            elif choice == '3':
                car = Car()
            else:
                print('Enter 1, 2, or 3.')

        car.get_user_input()
        inventory.append(car)
        response = input('Again? (y/n) ')

    display_inventory(inventory)
    save_cars_to_file(inventory)

def load_cars_from_file():
    inventory = []
    try:
        cars_file = open('cars.dat', 'rb')
        inventory = pickle.load(cars_file)
        cars_file.close()
    except FileNotFoundError:
        pass

    return inventory

def save_cars_to_file(inventory):
    cars_file = open('cars.dat', 'wb')
    pickle.dump(inventory, cars_file)
    cars_file.close()
    print('File cars.dat was updated.')

def display_inventory(inventory):
    if len(inventory) != 0:
        cars_str = ''
        for car in inventory:
            print(car)
    else:
        print('Car lot is empty.')


main()
