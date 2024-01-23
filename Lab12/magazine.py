#
# Aleem Azimov
# 11/12/2022
# Create a sub class named Magazine that inherits from superclass InventoryItem
#
from inventory_item import InventoryItem


class Magazine(InventoryItem):
    def __init__(self, name='', count=0, cost=0.0, description='', upc='', supp_code=''):
        super().__init__(name, count, cost, description)
        self.upc = upc
        self.supp_code = supp_code

    def get_item_input(self):
        super().get_item_input()
        while True:
            self.upc = input('What is the UPC?: ')
            if not (len(self.upc) == 12 and self.upc.isdigit()):
                print('UPC must have 12 digit characters')
            else:
                break
        while True:
            self.supp_code = input('What is the Supplemental Code?: ')
            if not (len(self.supp_code) == 2 and self.supp_code.isdigit()):
                print('Supplemental code must have 2 digit characters')
            else:
                break
        print('')

    def __str__(self):
        return super().__str__() + f'\n\tUPC: {self.upc}, Supplemental Code: {self.supp_code}'
