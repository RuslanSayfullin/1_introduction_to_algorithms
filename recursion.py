def matryoshka(n):
    if n==1:
        print("Матрёшка")
    else:
        print ("Вверх матрёшки", n)
        matryoshka(n-1)
        print("Низ матрёшки n=", n)

