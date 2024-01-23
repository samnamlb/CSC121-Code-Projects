# Creating and using lists from dictionaries

car_year = {"Toyota RAV4": 2019,
            "Ford Ranger": 2015,
            "Honda CR-V": 2018,
            "Lincoln Towncar": 2013,
            "Chevy Volt": 2020}

keys = car_year.keys()
keys_list = list(keys)
print(keys_list)

values_list = list(car_year.values())
earliest = min(values_list)
print(earliest)

items_list = list(car_year.items())
print(items_list)
