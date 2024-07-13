def func(lst):
    lst = list(sorted(set(lst)))
    min2 = lst[1]
    print(lst)
    return min2

son = [15, 23, 14, 75, 32, 14, 23, 65, 89, 41, 1]
print(func(son))

