def lefenstein(a, b):
    """алгоритм редакционного растояния"""
    f = [[(i+j) if i*j == 0 else 0 for j in range(len(a))]for i in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = 1+min(f[i-1][j], f[i][j-1], f[i-1][j-1])
    return f[len(a)][len(b)]

def equal(a, b):
    """Проверка равенства строк"""
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

def search_substring(s, sub):
    """поиск подстроки в строке"""
    for i in range(0, len(s) - len(sub)):
        if equal(s[i:i+len(sub)], sub):
            print(i)