def check_sorted(a, aserding=True):
    """Проверка отсортерованности за o(len(a))"""
    n = len(a)
    flag = True
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            flag = False
            break
    return flag