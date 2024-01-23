#
# Aleem Azimov
# September 15, 2022
# Creating and manipulating lists
#
import random


# list generator, generates a list between 1 to 15
def generate_list(max_num):
    num_list = []
    for i in range(max_num):
        number = random.randint(1, 15)
        num_list.append(number)
    return num_list


# Compares each list by largest num by each index
def compare_by_largest_num(list1, list2):
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            print(f"{list1[i]} : First List")
        elif list1[i] < list2[i]:
            print(f"{list2[i]} : Second List")
        else:
            print(f"{list1[i]} : Equal")


def main():
    # Step a
    count = int(input("Step a: How many numbers in each list? "))

    list1 = generate_list(count)
    list2 = generate_list(count)
    # Step b
    print(f"Step b: First list: {list1}")
    # Step c
    print(f"Step c: Second list: {list2}")
    # Step d
    print("Step d:\nLarger number in each comparison:")
    compare_by_largest_num(list1, list2)
    # Step e
    concat_list = list1 + list2
    print(f"Step e: Combined List: {concat_list}")
    # Step f
    concat_list.sort()
    print(f"Step f: Sorted list: {concat_list}")
    # Step g
    print("Step g:")
    print(f"First three elements: {concat_list[:3]}")
    print(f"Last three elements: {concat_list[-3:]}")
    # Step h
    print("Step h:")
    for i in range(4):
        number = random.randint(1, 15)
        if number in concat_list:
            print(f"{number} in index {concat_list.index(number)}")
            concat_list.remove(concat_list[concat_list.index(number)])
        else:
            print(f"{number} not found in list")

    # Step i
    print(f"Step i: Final list: {concat_list}")


main()
