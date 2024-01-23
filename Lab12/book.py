#
# Aleem Azimov
# 11/12/2022
# Create a sub class named Book that inherits from superclass InventoryItem
#
from inventory_item import InventoryItem


class Book(InventoryItem):
    def __init__(self, name='', count=0, cost=0.0, description='', isbn13=''):
        super().__init__(name, count, cost, description)
        self.isbn13 = isbn13

    def get_item_input(self):
        super().get_item_input()
        while True:
            self.isbn13 = input('What is the ISBN?: ')
            if not (len(self.isbn13) == 13 and self.isbn13.isdigit()):
                print('ISBN must have 13 digit characters')
            else:
                break
        print('')

    def __str__(self):
        return super().__str__() + f'\n\tISBN: {self.isbn13}'
