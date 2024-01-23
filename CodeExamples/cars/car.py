#
# James Matlock
# Apr 7, 2022
# Example for Lesson 12: This class represents a generic car in our inventory.
#

class Car:
    def __init__(self, name='', year=0, price=0.0):
        self.name = name
        self.year = year
        self.price = price

    def get_user_input(self):
        self.name = input('Enter name of car: ')
        self.year = int(input('Enter year of car: '))
        self.price = float(input('Enter price of car: '))

    def __str__(self):
        return f'Name: {self.name}, Year: {self.year}, Price: {self.price}'
