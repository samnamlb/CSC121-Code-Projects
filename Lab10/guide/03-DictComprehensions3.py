# Examples of doing dictionary comprehensions

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d2 = {v: k for k, v in d1.items()}
print(d2)

d2 = {}
for k, v in d1.items():
    d2[v] = k
print(d2)

