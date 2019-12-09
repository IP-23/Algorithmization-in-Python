# Вычисление суммы ряда, который имеет вид: 1 -0.5 0.25 -0.125 ...


def recursion(n=int(input('Введите количество членов последовательности: '))):
    if n == 1:
        return 1
    else:
        return ((-1) ** (n-1)) * (1/(2**(n-1))) + recursion(n-1)


print(recursion())
