#возвращает рекурсивно число фиббоначи
def fib(n: int):
    assert n >= 0
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

# вычисляется число фиббоначи динамический
def fib2(n: int):
    assert n >= 0
    fib = [None]*(n+1)
    fib[:2] = [0,1]
    for k in range(2, n+1):
        fib[k] = fib[k-1]+fib[k-2]
    return fib[n]
