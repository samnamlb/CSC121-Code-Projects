#
# Aleem Azimov
# September 24, 2022
# Generate a line graph from user inputs and matplotlib
#
import matplotlib.pyplot as plt


def main():
    x_values = [1, 2, 3, 4, 5]
    y_values = []
    days_week = []
    chart_title = input("Enter the line graph title: ")
    x_label = input("Enter the label for the x-axis: ")
    y_label = input("Enter the label for the y-axis: ")

    for i in range(5):
        tick = input(f"Enter the name for tick {i + 1}: ")
        value = float(input(f"Enter the value for tick {i + 1}: "))
        y_values.append(value)
        days_week.append(tick)

    plt.plot(x_values, y_values, marker='o')

    plt.title(chart_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(x_values, days_week)
    plt.grid(True)
    plt.show()


main()
