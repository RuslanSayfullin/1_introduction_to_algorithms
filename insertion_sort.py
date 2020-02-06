def insertion_sort_1(a):
    """сортировка списка a вставками, по возрастанию"""
    n = len(a)
    for k in range(1, n):
        while k > 0 and a[k-1] > a[k]:
            a[k], a[k-1] = a[k-1], a[k]
            print(k)
            k -= 1
    print(a)

def insertion_sort_2(a):
    """сортировка списка A вставками, по убыванию"""
    n = len(a)
    for k in range(1, n):
        while k > 0 and a[k-1] < a[k]:
            a[k], a[k-1] = a[k-1], a[k]
            k -= 1
    print(a)
    
def test_sort_1(sort_algorithm):
    print("testcase#1: ", end=" ")
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    print("Ok" if a == a_sorted else "Fail")

def test_sort_2(sort_algorithm):
    print("testcase#1: ", end=" ")
    a = [4, 2, 5, 1, 3]
    a_sorted = [5, 4, 3, 2, 1]
    sort_algorithm(a)
    print("Ok" if a == a_sorted else "Fail")

if __name__ == '__main__':
    test_sort_1(insertion_sort_1)
    test_sort_2(insertion_sort_2)
