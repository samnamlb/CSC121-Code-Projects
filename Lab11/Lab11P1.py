#
# Aleem Azimov
# 11/5/2022
# Implement and test implementations of classes and create objects from Trish's bookstore
#
from inventory_item import InventoryItem


def main():
    science_book = InventoryItem('Science Book', 10, 12.90, 'Textbook for SCI 100')
    math_book = InventoryItem('Math Book', 15, 13.95, 'Activity book for K-3')
    fiction_book = InventoryItem('Fiction Book', 32, 7.00, 'Sci-fi classic')
    new_book = InventoryItem()

    new_book.get_item_input()
    print(science_book)
    print(math_book)
    print(fiction_book)
    print(new_book)


main()
