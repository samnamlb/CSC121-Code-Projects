##
# Aleem Azimov
# September 10, 2022
# Trish's Bookstore Calculator
#
# Global Constants
WORKBOOK_COST = 8.50
TEXTBOOK_COST = 24.00
MAGAZINE_COST = 5.95
TAX_RATE = 0.06  # Tax Rate of 6%


def main():  # DO NOT CHANGE ANY CODE IN THE MAIN ROUTINE
    # NOTE: This program is NOT doing input validation to simplify the
    # program. To do input validation we would need to insert these lines
    # into while loops.
    num_wbs = int(input('Enter the number of workbooks: '))
    num_tbs = int(input('Enter the number of textbooks: '))
    num_mags = int(input('Enter the number of magazines: '))

    calc_and_display_total(num_wbs, num_tbs, num_mags)


# Create a function called calc_and_display_total. It should take
# 3 parameters. Use the names provided here:
#    workbooks  - Number of workbooks
#    textbooks  - Number of textbooks
#    magazines  - Number of magazines
#
# It should calculate and display the total cost of each item. It should also
# calculate and display the total cost with tax.

def calc_and_display_total(workbooks, textbooks, magazines):
    workBookTotal = workbooks * WORKBOOK_COST

    textBookTotal = textbooks * TEXTBOOK_COST

    magazineTotal = magazines * MAGAZINE_COST

    subtotal = workBookTotal + textBookTotal + magazineTotal

    tax = subtotal * TAX_RATE

    total = subtotal + tax

    print(f"Workbooks: ${workBookTotal:.2f}")
    print(f"Textbooks: ${textBookTotal:.2f}")
    print(f"Magazines: ${magazineTotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")


main()
