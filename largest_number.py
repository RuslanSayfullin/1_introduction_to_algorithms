#нахождение наибольшего целого числа
def array1(a):
    largest=a[0]
    n= len(a)
    for i in range(1, n):
        if a[i] > largest:
            largest=a[i]
    return(largest)
            
            
            
def test_largest(test_algorithm):
    print("trstcase#1 ", end=" ")
    a=[1, 5, 2]
    test_algorithm(a)
    print( "Ok" if test_algorithm(a)==5  else "Fail")

if __name__ == '__main__':
    test_largest(array1)

