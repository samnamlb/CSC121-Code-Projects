#
# Aleem Azimov
# 10/6/2022
# Count uppercase letters in a string
#
import os

# DO NOT CHANGE ANY CODE IN THE MAIN FUNCTION
def main():
    try:
        input_file = open('strings.txt', 'r')  # Open a file for reading
        for line in input_file:  # Use a for loop to read each line in the file
            manipulate_text(line)
            print()
    except FileNotFoundError:
        print('Did not find strings.txt in current directory:')
        print(os.getcwd())


def manipulate_text(line):
    used_letters = []
    line = line.strip()
    print(line)
    line = line.replace(' ', '')

    for letter in line:
        if letter not in used_letters and letter.isalpha() and letter.isupper():
            frequency = line.count(letter)
            print(f'{letter} {frequency}')
            used_letters.append(letter)



main()
