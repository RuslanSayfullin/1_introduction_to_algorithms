def euclidean_theorem(a,b):
    """Алгоритм нахождения НОД двух
    чисел, не использующий перебор."""
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    gcd = a
    print(gcd)

def euclidean_theorem_2(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    gcd = a+b
    print(gcd)

def greatest_common_divisor():
    """задача определения наибольшего
    общего делителя (НОД) двух натуральных чисел"""
    print("Задайте первое число")
    a = int(input())
    print("Задайте второе число")
    b = int(input())
    if a > b:
        max = a
        min = b
    else:
        max = b
        min = a

    remainder = max % min
    while remainder != 0:
        max = min
        min = remainder
        remainder =max % min
    gcd=min
    print(gcd)

def GCD(a,b):
    """Алгоритм нахождения НОД двух чисел."""
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    print(GCD)

