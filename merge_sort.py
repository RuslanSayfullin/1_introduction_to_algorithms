def merge_sort0(a: list, b: list):
    """"Сортировка слиянием 2-х массивов(списков)"""
    c = [0]*(len(a)+len(b))
    i = k = n = 0   # инициализируем 3 счетчика
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
        
    "Если один из массивов опустел"
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    print (c)

#Рекурсивная функция
def merge_sort1(a):
    """сортировка списка а методом слияния"""
    if len(a) <= 1:
        return
    middle = len(a)//2
    left = [a[i] for i in range(0, middle)]
    right = [a[i] for i in range(middle, len(a))]
    merge_sort1(left)
    merge_sort1(right)
    c = merge_sort0(left, right)
    a = c[:]
    print(a)


def test_merge_sort0(sort_algorithm):
    print("testcase#1: ", end=" ")
    a = [1, 9, 12]
    b = [3, 11]
    c_sorted = [1, 3, 9, 11, 12]
    sort_algorithm(a, b)
    print("Ok" if c_sorted == merge_sort1(a, b) else "Fail")

def test_merge_sort1(sort_algorithm):
    print("testcase#0 : ", end=" ")
    a = [1, 9, 12, 3, 11]
    c_sorted = [1, 3, 9, 11, 12]
    sort_algorithm(a)
    print("Ok" if c_sorted == merge_sort0(a) else "Fail")

if __name__ == '__main__':
    test_merge_sort0(merge_sort0)
    test_merge_sort1(merge_sort1)

