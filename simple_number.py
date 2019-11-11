def is_simple_number(x):
    """определяет, является ли число простым.
    x- целое положительное число.
    Если простое, то возврощает True.
    а иначе False
    """

    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True
