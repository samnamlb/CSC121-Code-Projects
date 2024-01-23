#
# James Matlock
# Apr 7, 2022
# Example for Lesson 12: This class represents a car in our inventory that
# runs on electricity.
#

from car import Car

class ElectricCar(Car):
    def __init__(self, name='', year=0, price=0.0,
                 time_to_charge=0, miles_per_charge=0):
        super().__init__(name, year, price)
        self.time_to_charge = time_to_charge
        self.miles_per_charge = miles_per_charge

    def get_user_input(self):
        super().get_user_input()
        self.time_to_charge = int(input('Enter time (in min) to charge battery: '))
        self.miles_per_charge = int(input('Enter total miles on full charge: '))

    def __str__(self):
        return super().__str__() + \
               f', Charge Time: {self.time_to_charge} minutes' + \
               f', Range: {self.miles_per_charge} miles'
