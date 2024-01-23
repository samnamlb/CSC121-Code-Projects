# Examples of doing dictionary comprehensions

cubes = {}
for i in range(1, 11):
    cubes[i] = i ** 3
print(cubes)

cubes = {i: i ** 3 for i in range(1, 11)}
print(cubes)
