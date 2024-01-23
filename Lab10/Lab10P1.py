#
# Aleem Azimov
# 10/28/22
# Demonstrates ability to use dictionary comprehensions
#

def main():
    text = input('Enter a string: ').upper()

    letter_count = {letter: text.count(letter) for letter in text if letter.isalpha()}
    print(f'Letter Count: {letter_count}')

    max_count = max(letter_count.values())

    letter_count_max = {key: value for key, value in letter_count.items() if value == max_count}
    print(f'Letter Max: {letter_count_max}')


main()
