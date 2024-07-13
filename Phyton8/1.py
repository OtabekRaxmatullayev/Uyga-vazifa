def func(lst):
    lst = list(sorted(set(lst)))
    max2 = lst[-2]
    print(lst)
    return max2

son = [15, 23, 14, 75, 32, 14, 23, 65, 89, 41, 1]
print(func(son))

