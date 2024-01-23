#
# Aleem Azimov
# 11/12/2022
# Extend InventoryItem class to support Books and Magazines using classes
#
from inventory_item import InventoryItem
from book import Book
from magazine import Magazine


def main():
    item_list = []
    book_mark = InventoryItem('Bookmark', 250, 1.00, 'Marker for books')
    sci_book = Book('Science Book', 100, 22.95, 'First year textbook', '2345234523451')
    fic_book = Book('Fiction Novel', 150, 8.95, 'Classic stories', '3456345634561')
    time_magazine = Magazine('Time', 75, 6.95, 'Weekly news', '123456789012', '12')
    consumer_magazine = Magazine('Consumers Report', 50, 5.95, 'Monthly articles', '098765432121', '99')
    for i in range(3):
        choice = ''
        while choice not in ['1', '2', '3']:
            choice = input('What item type (1-Book, 2-Magazine, 3-Other)? ')
            if choice == '1':
                item = Book()
            elif choice == '2':
                item = Magazine()
            elif choice == '3':
                item = InventoryItem()
            else:
                print('Enter 1, 2, or 3')
        item.get_item_input()
        item_list.append(item)
    print('')
    print(book_mark)
    print(sci_book)
    print(fic_book)
    print(time_magazine)
    print(consumer_magazine)
    print('')
    print('Prompted Items:')
    for item in item_list:
        print(item)


main()
