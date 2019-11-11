def eratosthenes_sieve(max_number):
    """Находим простые числа между 2 и max_number(включительно). Данный алгоритм обладает временем работы O(N*log(logN))"""
    ##Определяем массив,куда закладываем булианы.
    is_composite=bool([True]*max_number)
    #замена на False начинается с 3-го элемента (первые два уже False)
    is_composite[0]=False
    is_composite[1]=False
    for k in range (2, max_number):
        if is_composite[k]: #писать if is_composite[k]=True не нужно, но можно.
            for i in range(2*k,max_number,k):
                is_composite[i]=False
    for k in range(is_composite):
        print(k,'-',"простое" if is_composite[k] else "составное")







