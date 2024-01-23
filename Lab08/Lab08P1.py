#
# Aleem Azimov
# 10/15/2022
# Read from csv, read item data, and display entries
#

def main():
    # Opens file inventory.csv, tests if filename is valid
    try:
        file = open('inventory.csv', 'r')
    except FileNotFoundError:
        print('File inventory.csv not found')
        exit()

    # Goes through each line in file,
    # Gets item name, count, unit cost, price, and description
    for record in file:
        record = record.strip('\n')
        record_list = record.split(',')
        item_name = record_list[0]
        item_count = int(record_list[1])
        unit_price = float(record_list[2])
        description = record_list[3]
        # Prints the contents of file
        print(item_name)
        print(f'\t{item_count} in stock, ${unit_price:.2f}')
        print('\t' + description)

    file.close()


main()
