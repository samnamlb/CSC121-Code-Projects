#
# Aleem Azimov
# September 15, 2022
# This program calculates the total cost for items purchased at Bargain
# Used Books. The program outputs the total cost before tax, the sales tax,
# and the total after tax.
#

# Global Constants - Use these in your program where it makes sense
TAX_RATE = 0.06  # 6% sales tax
WB_MAX = 40
WB_COST = 8.50
TB_MAX = 10
TB_COST = 24.00
MAG_MAX = 25
MAG_COST = 5.95


# The get_item_count function takes one parameter:
#    max_allowed - Maximum number of items the user can enter
#
# This function will ask the user to enter the number of items and
# validate the number entered is between 0 and the max_allowed
# inclusive. The number of items the user enters is returned.
def get_item_count(max_allowed):  # You should fill in the parameters needed

    count = int(input("Enter the number of items: "))
    while count < 0 or count > max_allowed:
        print(f"Number of items must be between 0 and {max_allowed}.")
        count = int(input("Enter the number of items: "))
    return count


# The get_item_total function takes two parameters:
#     num_items - Number of items
#     unit_price - The cost of each item
#
# This function calculates the total cost for the items and
# returns that value.
def get_item_total(num_items, unit_price):  # You should fill in the parameters needed

    total = num_items * unit_price
    return total


# The calc_and_display_receipt function will calculate all the
# necessary values and display the receipt. It takes three parameters:
#    wb_total - Total cost of workbooks
#    tb_total - Total cost of textbooks
#    m_total  - Total cost of magazines
#
# This function will calculate total before tax, the tax on the total,
# and the total after tax is added.
#
# The receipt should display the total cost of workbooks, textbooks, and
# magazines IF the item cost is greater than 0. The receipt should also
# include the subtotal, tax, and total.
def calc_and_display_receipt(wb_total, tb_total, m_total):  # You should fill in the parameters needed

    subtotal = wb_total + tb_total + m_total
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print("")
    if wb_total > 0:
        print(f"Workbooks: ${wb_total:.2f}")
    if tb_total > 0:
        print(f"Textbooks: ${tb_total:.2f}")
    if m_total > 0:
        print(f"Magazines: ${m_total:.2f}")
    print("---------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Amount due: ${total:.2f}")


# main function - DO NOT MAKE ANY CHANGES TO CODE BELOW THIS LINE!
def main():
    print('Workbooks')
    wb_item_count = get_item_count(WB_MAX)
    wb_total = get_item_total(wb_item_count, WB_COST)
    print('Textbooks')
    tb_item_count = get_item_count(TB_MAX)
    tb_total = get_item_total(tb_item_count, TB_COST)
    print('Magazines')
    m_item_count = get_item_count(MAG_MAX)
    m_total = get_item_total(m_item_count, MAG_COST)

    calc_and_display_receipt(wb_total, tb_total, m_total)


# Call the main function.
main()
