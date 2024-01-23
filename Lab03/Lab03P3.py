#
# Aleem Azimov
# September 3, 2022
# This program will help to calculate the cost of the total purchase for the customer
#

# named constants
TAX_RATE = 0.06
WORKBOOK_COST = 8.50
TEXTBOOK_COST = 24.00
MAGAZINE_COST = 5.95

# inputs that prompt for number of workbooks, magazines, and textbooks
numWorkBooks = int(input("Enter the number of workbooks: "))

# workbooks must be between 0 and 40
while numWorkBooks < 0 or numWorkBooks > 40:
    print("Number of workbooks must be between 0 and 40.")
    numWorkBooks = int(input("Enter the number of workbooks: "))

numTextBooks = int(input("Enter the number of textbooks: "))

# textbooks must be between 0 and 10
while numTextBooks < 0 or numTextBooks > 10:
    print("Number of textbooks must be between 0 and 10.")
    numTextBooks = int(input("Enter the number of textbooks: "))

numMagazines = int(input("Enter the number of magazines: "))

# magazines must be between 0 and 25
while numMagazines < 0 or numMagazines > 25:
    print("Number of magazines must be between 0 and 25.")
    numMagazines = int(input("Enter the number of magazines: "))

# processing step, calculates subtotal, sales tax, and total after tax
subtotal = (numWorkBooks * WORKBOOK_COST) + (numTextBooks * TEXTBOOK_COST) + (numMagazines * MAGAZINE_COST)

salesTax = subtotal * TAX_RATE

total = subtotal + salesTax

# output step, outputs subtotal, sales tax, and total after
print(f"Cost before tax: ${subtotal:.2f}")
print(f"Sales tax: ${salesTax:.2f}")
print(f"Cost after tax: ${total:.2f}")
