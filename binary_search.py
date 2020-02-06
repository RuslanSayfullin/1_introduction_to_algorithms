# массив должен быть отсортирован.
# возвращает индекс искомого значения.

def left_bound(a, key):
    left = -1
    right = len(a)
    while right-left > 1:
        middle = (left+right)//2
        if a[middle] < key:     # <= если ищем правое
            left = middle
        else:
            right = middle
    return left

def test_1(binary_algorithm):
    print("testcase#1: ", end=" ")
    a = [4, 2, 5, 1, 3]
    key = 1
    binary_algorithm(a)
    print("Ok" if a == key else "Fail")

if __name__ == '__main__':
    test_1(left_bound)