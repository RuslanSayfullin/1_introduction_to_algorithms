def array_search(a: list, n: int, x: int):
    """осуществляет поиск числа x в массиве А
    от 0 до N-1 индекса включительно.
    возвращает индекс элемента x в массиве A.
    Или -1, если такого нет.
    Если в массиве несколько элементов равных х,
    то вернуть первого по счёту"""
    for k in range(n):
        if a[k] == x:
            return k
    return -1

def test_array_search1(search_algorithm):
    a1 = [1, 2, 3, 4, 5]
    m = array_search(a1, 5, 2)
    if m == 1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

def test_array_search2(search_algorithm):
    a2 = [-1, -2, -3, -4, -5]
    m = array_search(a2, 5, -3)
    if m == 2:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

def test_array_search3(search_algorithm):
    a3 = [10, 20, 30, 10, 10]
    m = array_search(a3, 5, 10)
    if m == 0:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

if __name__ == '__main__':
    test_array_search1(array_search)
    test_array_search2(array_search)
    test_array_search3(array_search)