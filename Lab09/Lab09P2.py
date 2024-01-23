#
# Aleem Azimov
# 10/22/2022
# Demonstrate working with sets
#
import random


def gen_set():
    set_nums = set()
    for i in range(5):
        rand_num = random.randint(1, 15)
        set_nums.add(rand_num)
    return set_nums


def main():
    set1 = gen_set()
    print(f'set1: {set1}')
    set2 = gen_set()
    print(f'set1: {set2}')
    union_set = set1 | set2
    print(f'Union of set1 and set2: {set1 | set2}')
    print(f'Intersection of set1 and set2: {set1 & set2}')
    print(f'Difference of set1 and set2: {set1 - set2}')
    print(f'Symmetric difference of set1 and set2: {set1 ^ set2}')

    set3 = [elem for elem in union_set if elem < 9]
    print(f'Less than 9 in union of set1 and set2: {set3}')


main()
