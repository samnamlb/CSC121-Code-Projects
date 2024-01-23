# Examples of doing dictionary comprehensions

temperatures = {'Monday': 88.2,
                'Tuesday': 79.1,
                'Wednesday': 74.0,
                'Thursday': 92.4,
                'Friday': 76.8,
                'Saturday': 74.0,
                'Sunday': 80.3}

warm_temp = {}
for k in temperatures:
    if temperatures[k] >= 80:
        warm_temp[k] = temperatures[k]
print(warm_temp)

warm_temp = {k: temperatures[k] for k in temperatures if temperatures[k] >= 80}
print(warm_temp)
