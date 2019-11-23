# Вывод зеркального числа


def recursion(number=int(input('Введите натуральное число: '))):
    if len(str(number)) == 1:
        return number % 10
    else:
        return str(number % 10) + str(recursion(number // 10))


print(recursion())
