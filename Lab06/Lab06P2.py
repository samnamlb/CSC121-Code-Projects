#
# Aleem Azimov
# September 24, 2022
# Create and modify tuples
#
import random


def main():
    num_tuples = []
    values = int(input("How many values to put in tuple? "))
    start = int(input("What is the start of the range? "))
    end = int(input("What is the end of the range? "))

    for i in range(values):
        num = random.randint(start, end)
        num_tuples.append(num)
    num_tuples = tuple(num_tuples)
    print(f"Tuple of {values} random numbers: {num_tuples}")

    first_three = num_tuples[:3]
    print(f"Tuple of first 3 numbers: {first_three}")
    last_three = num_tuples[4:]
    print(f"Tuple of last 3 numbers: {last_three}")

    concat_tuple = first_three[:] + last_three[:]
    print(f"Two tuples concatenated: {concat_tuple}")
    concat_tuple = list(concat_tuple)
    concat_tuple.sort()
    concat_tuple = tuple(concat_tuple)
    print(f"Two tuples concatenated and sorted: {concat_tuple}")


main()
