def count_sort(a):
    """сортировка списка a методом подсчета"""
    pass



def test_sort_1(sort_algorithm):
    print("testcase#1: ", end=" ")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")


if __name__ == '__main__':
    test_sort_1(count_sort)