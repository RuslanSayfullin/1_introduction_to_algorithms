#возвращает рекурсивно число фиббоначи
def fib(n: int):
    assert n >= 0
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
    return fib[n]

# вычисляется число фиббоначи динамический
def fib2(n: int):
    assert n >= 0
    fib = [None]*(n+1)
    fib[:2] = [0,1]
    for k in range(2, n+1):
        fib[k] = fib[k-1]+fib[k-2]
    return fib[n]

def test_fib(algorithm):
    print("testcase#0 : ", end=" ")
    n = 9
    number = 34
    algorithm(n)
    print("Ok" if number == n else "Fail")

if __name__ == '__main__':
    test_fib(fib)