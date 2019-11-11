def bubble_sort(A):
    """сортировка списка А методом пузырька"""
    N =len(A)
    for bypass in range(1, N):
        for k in range (0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1]=A[k+1], A[k]
    

def test_sort_1(sort_algorithm):
    print("testcase#1: ", end=" ")
    A= [4, 2, 5, 1, 3]
    A_sorted=[1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A ==A_sorted else "Fail")


if __name__=='__main__':
    test_sort_1( bubble_sort)

