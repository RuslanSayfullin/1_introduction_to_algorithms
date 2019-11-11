# массив должен быть отсортирован.
# возвращает индекс искомого значения.

def left_bound(a, key):
    left=-1
    right = len(a)
    while right-left >1:
        middle = (left+right)//2
        if a[middle] <key: # <= если ищем правое
            left = middle
        else:
            right=middle
    return right