#
# James Matlock
# Apr 7, 2022
# Example for Lesson 12: This program will provide a test for the Car classes
# that have been implemented.
#

from car import Car
from gasCar import GasCar
from electricCar import ElectricCar

def main():
    car1 = Car('Generic', 2000, 3005.33)
    car2 = GasCar('Honda CR-V', 2015, 23033.22, 12, 33)
    car3 = ElectricCar('Chevy Volt', 2021, 32839.95, 240, 400)

    choice = input('What type of car do you want to add? (1-Gas, 2-Electric, 3-Other) ')

    if choice == '1':
        car4 = GasCar()
    elif choice == '2':
        car4 = ElectricCar()
    else:
        car4 = Car()
    car4.get_user_input()

    print(car1)
    print(car2)
    print(car3)
    print(car4)

main()
