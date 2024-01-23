#
# James Matlock
# Apr 7, 2022
# Example for Lesson 12: This program will extend the example we did in Lesson
# 11 and demonstrate using our Car classes in a simple inventory program. In
# example, Car objects (and their derived versions) are kept in a CarLot class
# which supports saving and loading to a file and displaying the inventory.
#

from car import Car
from gasCar import GasCar
from electricCar import ElectricCar
from carLot import CarLot

def main():
    car_inventory = CarLot()
    car_inventory.load_cars_from_file()
    print(car_inventory)

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
        car_inventory.add_car(car)
        response = input('Again? (y/n) ')

    print(car_inventory)
    car_inventory.save_cars_to_file()

main()
