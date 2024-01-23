#
# James Matlock
# Apr 7, 2022
# Example for Lesson 12: This class represents a car in our inventory that
# runs on gas.
#

from car import Car

class GasCar(Car):
    def __init__(self, name='', year=0, price=0.0, gallons=0, mpg=0):
        super().__init__(name, year, price)
        self.gallons = gallons
        self.mpg = mpg

    def get_user_input(self):
        super().get_user_input()
        self.gallons = int(input('Enter number of gallons to fill the tank: '))
        self.mpg = int(input('Enter the miles per gallon: '))

    def __str__(self):
        return super().__str__() + f', Gallons: {self.gallons}, MPG: {self.mpg}'
