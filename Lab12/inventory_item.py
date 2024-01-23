#
# Aleem Azimov
# 11/12/2022
# Create an InventoryItem superclass as a base for sub classes to use
#

class InventoryItem():
    def __init__(self, name='', count=0, cost=0.0, description=''):
        self.name = name
        self.count = count
        self.cost = cost
        self.description = description

    def get_item_input(self):
        self.name = input('Enter the item name: ')
        while True:
            try:
                self.count = int(input('Enter the item count: '))
                if self.count < 0:
                    print('Item count must be 0 or greater.')
                else:
                    break
            except:
                print('Item count must be an integer.')
        while True:
            try:
                self.cost = float(input('Enter the unit cost: '))
                if self.cost < 0:
                    print('Unit cost must be 0 or greater.')
                else:
                    break
            except:
                print('Unit cost must be an integer.')
        self.description = input('Enter the description: ')

    def get_retail_value(self):
        return self.count * self.cost

    def __str__(self):
        return f'{self.name}\n\tCount: {self.count}, Cost: {self.cost:.2f}, Retail Value: {InventoryItem.get_retail_value(self):.2f}\n\t{self.description} '
