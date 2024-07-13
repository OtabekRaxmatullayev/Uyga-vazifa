def func(d, key):
    if key in d:
        del d[key]
    return d

dic = {'a': 10, 'f': 14, 'b': 20, 'c': 5}
print(func(dic,'b'))
