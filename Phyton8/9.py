def func(dict):
    dict1 = {value: key for key, value in dict.items()}
    return dict1

dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(func(dict2))
