def choise_sort(A):
    """сортировка списка A выбором"""
    N=len(A)
    for pos in range(0,N-1):
        for k in range(pos+1, N):
            if A[k]<A[pos]:
                A[k], A[pos]=A[pos], A[k]
        
    print(A)


def test_sort(sort_algorithm):
    print("testcase#1: ", end=" ")
    A= [4, 2, 5, 1, 3]
    A_sorted=[1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A ==A_sorted else "Fail")

if __name__=='__main__':
    test_sort(choise_sort)
