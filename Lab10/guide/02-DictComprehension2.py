# Examples of doing dictionary comprehensions

grades = {'Fred': [95, 100, 84],
          'Maria': [98, 93, 95, 90],
          'Bob': [82, 77, 75]}

averages = {}
for k, v in grades.items():
    averages[k] = sum(v) / len(v)
print(averages)

averages = {k: sum(v) / len(v) for k, v in grades.items()}
print(averages)
