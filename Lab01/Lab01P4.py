#
# Aleem Azimov
# August 24, 2022
# This program will help to calculate the cost of the total purchase for the customer
#

# named constant of tax rate %6
TAX_RATE = 0.06
WORKBOOK_COST = 8.50
TEXTBOOK_COST = 24.00
MAGAZINE_COST = 5.95

# inputs that prompt for number of workbooks, magazines, and textbooks
numWorkBooks = float(input("Enter the number of workbooks: "))
numTextBooks = float(input("Enter number of textbooks: "))
numMagazines = float(input("Enter the number of magazines: "))

# processing step, calculates subtotal, sales tax, and total after tax
subtotal = (numWorkBooks * WORKBOOK_COST) + (numTextBooks * TEXTBOOK_COST) + (numMagazines * MAGAZINE_COST)

salesTax = subtotal * TAX_RATE

total = subtotal + salesTax

# output step, outputs subtotal, sales tax, and total after
print(f"Cost before tax: ${subtotal:.2f}")
print(f"Sales tax: ${salesTax:.2f}")
print(f"Cost after tax: ${total:.2f}")
