def invert_array(A:list, N:int):
    """Обоащение массива (поворот задом-наперёд)
    в рамках индексов от 0 до N-1"""
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]


def test_invert_array1(search_algorithm):
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_array(A1, 5)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

def test_invert_array2(search_algorithm):
    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(A2)
    invert_array(A2, 8)
    print(A2)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

if __name__ == '__main__':
    test_invert_array1(invert_array)
    test_invert_array2(invert_array)