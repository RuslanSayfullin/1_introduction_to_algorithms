# Сортировка Тони Хора(быстрая сортировка), выполняется по прямому ходу
# без дополнительной памяти. Алгоритм:"разделяй и властвуй"

def hoar_sort(a):
    if len(a) <= 1:
        return
    barrier = a[0]
    l, m, r = [], [], []
    for x in a:
        if x < globals():
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)
    hoar_sort(l)
    hoar_sort(r)

# переливаем обратно в list(a)
    k = 0
    for x in l+m+r:
        a[k] = x;
        k += 1



