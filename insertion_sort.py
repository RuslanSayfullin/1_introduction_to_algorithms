def insertion_sort_1(A):
    """сортировка списка A вставками, по возрастанию"""
    N=len(A)
    for top in range(1, N):
        k = top
        while k>0 and A[k-1]>A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
    print(A)

def insertion_sort_2(A):
    """сортировка списка A вставками, по убыванию"""
    N=len(A)
    for top in range(1,N):
        k=top
        while k>0 and A[k-1]<A[k]:
            A[k], A[k-1]=A[k-1], A[k]
            k-=1
    print(A)
    
def test_sort_1(sort_algorithm):
    print("testcase#1: ", end=" ")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A ==A_sorted else "Fail")

def test_sort_2(sort_algorithm):
    print("testcase#1: ", end=" ")
    A= [4, 2, 5, 1, 3]
    A_sorted=[5, 4, 3, 2, 1]
    sort_algorithm(A)
    print("Ok" if A ==A_sorted else "Fail")

if __name__=='__main__':
    test_sort_1(insertion_sort_1)
    test_sort_2(insertion_sort_2)
