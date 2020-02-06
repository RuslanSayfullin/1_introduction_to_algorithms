def choise_sort(a):
    """сортировка списка A выбором"""
    n = len(a)
    for pos in range(0, n-1):
        for k in range(pos+1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]
        
    print(a)


def test_sort(sort_algorithm):
    print("testcase#1: ", end=" ")
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    print("Ok" if a == a_sorted else "Fail")

if __name__ == '__main__':
    test_sort(choise_sort)
