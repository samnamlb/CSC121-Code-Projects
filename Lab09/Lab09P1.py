#
# Aleem Azimov
# 10/22/2022
# Demonstrate working with dictionaries
#

def main():
    file = open('strings.txt', 'r')

    for line in file:
        line = line.strip('\n').strip(' ').upper()
        dict_line = {}

        for letter in line:
            if letter.isalpha():
                dict_line[letter] = line.count(letter)

        min_count = [count for count in dict_line if dict_line[count] == 1]
        print(line)
        print(f'Dictionary: {dict_line}')
        print(f'Letters with min count of 1: {min_count}')

        for letter in min_count:
            del dict_line[letter]

        print(f'Dictionary after min letter removed: {dict_line}')
        list_dict = [letter for letter in dict_line]
        list_dict.sort()
        print(f'Letters sorted: {list_dict}\n')


main()
