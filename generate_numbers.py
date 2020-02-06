def generate_numbers(N:int, M:int, prefix= None):
    """генерация всех перестановок
    N-основание счисления, M-кол-во чисел"""
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return

    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

