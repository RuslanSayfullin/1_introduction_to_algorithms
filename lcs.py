# A и B -массивы чисел len(A)==N, len(B)==M
#Подпоследовательность A: массив C содержащий элементы A, во входном порядке, но возможно не все.
def largest_common_subsequence(a, b):
    """lcs наибольшая общая подпоследовательность"""
    f = [[0]*(len(b)+1)for i in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1]== b[j-1]:
                f[i][j]=1+f[i-1][j-1]
            else:
                f[i][j] = max(f[i-1][j], f[i][j-1])
        return f[-1][-1]

# найбольшая возоастающая подпоследовательность
def dis(a):
    f = [0]*(len(a)-1)
    for i in range(1, len(a)-1):
        m = 0
        for j in range(0, i):
            if a[i] > a[j] and f[j]>m:
                m = f[j]
        f[i] = m+1
        return f(callable(a))
