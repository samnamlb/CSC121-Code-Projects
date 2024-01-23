#
# Aleem Azimov
# August 27, 2022
# Add discount for customers based on their loyalty program membership and how much they spend. Calculate sales tax and total.
#

TAX = 0.06

# Get user's purchase price
userPurchase = float(input("Enter the total purchase amount: "))

# Ask user if they are in a loyalty program
userLoyalty = str(input("Is the customer a loyalty program member (y/n): "))

# Determines if customer is a loyalty member
isLoyal = True if userLoyalty == "y" else False

# When the user is a loyal member, test whether their purchase is over or under $100
if isLoyal == True:

    # If the purchase is equal or below $100, user gets a 15% discount. Else, user gets a 25% discount
    if userPurchase <= 100:
        discount = 0.15
    else:
        discount = 0.25
else:

    # If the user is not a loyal member and their purchase is over $100, user gets a 5% discount
    if userPurchase > 100:
        discount = 0.05

# Calculates total after discount, BEFORE tax
subtotal = userPurchase - (userPurchase * discount)

# Calculates sales tax
salesTax = subtotal * TAX

# Calculates total with sales tax
total = salesTax + subtotal

# Outputs total with discount, sales tax, and net total
print(f'Total after discount: ${subtotal:.2f}')
print(f'Sales tax: ${salesTax:.2f}')
print(f'Total after tax: ${total:.2f}')
