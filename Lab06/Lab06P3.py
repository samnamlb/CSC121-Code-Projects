#
# Aleem Azimov
# September 24, 2022
# Use list comprehensions
#

def main():
    # Step a
    list1 = [3, 1, 4, 1, 5]
    list2 = [2, 5]

    # Step b
    list3 = [num * 3 - 2 for num in range(5)]

    # Step c
    list4 = [i - j for i in range(8) for j in range(4) if i % 2 == 1]

    # Step d
    list5 = [i ** i for i in list1]

    # Step e
    list6 = [i * 3 + 1 for i in list1]

    # Step f
    list7 = [i - j for i in list1 for j in list2]

    # Step g
    list8 = [f'{i}&{j}' for i in list1 for j in list2]

    print(f"Step b: {list3}")
    print(f"Step c: {list4}")
    print(f"Step d: {list5}")
    print(f"Step e: {list6}")
    print(f"Step f: {list7}")
    print(f"Step g: {list8}")


main()
