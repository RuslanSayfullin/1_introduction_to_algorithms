# Сортировка Тони Хора(быстрая сортировка), выполняется по прямому ходу
# без дополнительной памяти. Алгоритм:"разделяй и властвуй"

def hoar_sort(a):
    if len(a) <= 1:
        return
    barrier = a[0]
    l, m, r = [], [], []
    for x in a:
        if x < barrier:
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)
    print(l, m, r)
    hoar_sort(l)
    hoar_sort(r)

# переливаем обратно в list(a)
    k = 0
    a = l+m+r
    for x in range(len(a)):
        a[k] = x
        k += 1
    print(a)

def test_sort_1(sort_algorithm):
    print("testcase#1: ", )
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    print("Ok" if a == a_sorted else "Fail")


if __name__ == '__main__':
    test_sort_1(hoar_sort)

