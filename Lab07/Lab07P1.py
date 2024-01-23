#
# Aleem Azimov
# 10/6/2022
# Examine and manipulate strings
#

# returns true if there is at least one non-digit in a string
def check_non_digits(num_set):
    non_digit = False
    for i in num_set:
        if not (i.isdigit()):
            non_digit = True
    if non_digit:
        return True
    else:
        return False


def main():
    user_input = input('Enter phone number or q to quit: ')
    # exit when user puts 'q' or 'Q'
    while user_input.lower() != 'q':
        if user_input.count('-') != 2:
            print('Phone number should have 2 dashes.')
            user_input = input('Enter phone number or q to quit: ')
        else:
            # split phone number into three parts: first, second, last
            user_phone = user_input.split('-')
            first = user_phone[0]
            second = user_phone[1]
            last = user_phone[2]

            # determines if first part has three-digits
            if check_non_digits(first) or len(first) != 3:
                print('First part of phone number must be a 3-digit number.')
                user_input = input('Enter phone number or q to quit: ')
            # determines if second part has three-digits
            elif check_non_digits(second) or len(second) != 3:
                print('Second part of phone number must be a 3-digit number.')
                user_input = input('Enter phone number or q to quit: ')
            # determines if last part has four-digits
            elif check_non_digits(last) or len(last) != 4:
                print('Last part of phone number must be a 4-digit number.')
                user_input = input('Enter phone number or q to quit: ')
            # checks if first part is in range between 200 to 999
            elif int(first) > 999 or int(first) < 200:
                print('First 3 digits must be between 200 and 999.')
                user_input = input('Enter phone number or q to quit: ')
            else:
                # if valid phone, remove dashes and put in place '.'
                phone_no_dash = user_input.replace('-', '.')
                print(f'Phone number with dashes replaced: {phone_no_dash}')
                user_input = input('Enter phone number or q to quit: ')


main()
