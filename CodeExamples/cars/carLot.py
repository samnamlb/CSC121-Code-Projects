#
# James Matlock
# Apr 7, 2022
# Example for Lesson 12: This class keeps an inventory of the cars that
# we have on our car lot. It provides the ability to add cars to the
# inventory as well as the ability to save and load the inventory to a file
# so that the state can be maintained on the file system.
#

import pickle

class CarLot:
    def __init__(self):
        self.__cars = []

    def add_car(self, car):
        self.__cars.append(car)

    def load_cars_from_file(self):
        try:
            cars_file = open('cars.dat', 'rb')
            self.__cars = pickle.load(cars_file)
            cars_file.close()
        except FileNotFoundError:
            pass

    def save_cars_to_file(self):
        cars_file = open('cars.dat', 'wb')
        pickle.dump(self.__cars, cars_file)
        cars_file.close()
        print('File cars.dat was updated.')

    def __str__(self):
        if len(self.__cars) != 0:
            cars_str = ''
            for car in self.__cars:
                cars_str += str(car) + '\n'
            return cars_str
        else:
            return 'Car lot is empty.'

