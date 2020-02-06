def bubble_sort(a):
    """сортировка списка А методом пузырька"""
    n = len(a)
    for pos in range(1, n):
        for k in range(0, n-pos):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]
    

def test_sort_1(sort_algorithm):
    print("testcase#1: ", end=" ")
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    print("Ok" if a == a_sorted else "Fail")


if __name__ == '__main__':
    test_sort_1(bubble_sort)

