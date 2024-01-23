#
# Aleem Azimov
# 11/5/2022
# Implement classes and create objects from Trish's bookstore
#


class InventoryItem:

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
        print('')

    def __str__(self):
        return f'{self.name}\n\tCount: {self.count}, Cost: {self.cost:.2f}\n\t{self.description}'
