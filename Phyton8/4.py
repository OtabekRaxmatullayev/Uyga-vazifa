from collections import Counter

def func(sonlar):
    sanash = Counter(sonlar)
    qiymat = max(sanash.values())
    element = [k for k, v in sanash.items() if v == qiymat]
    return element

sonlar = [10, 20, 20, 4, 45, 20, 4, 4, 45, 3, 5]
print(', '.join(map(str, func(sonlar))))
