# Определить, какое число в массиве встречается чаще всего

from random import randint
try:
    LENGTH = int(input('Введите длину массива, который необходимо сформировать: '))
    USER_LIST = [randint(0, 5) for i in range(LENGTH)]    # формирование массива с случ. элементами от 0 до 5
    print(f'Исходный массив имеет вид: {USER_LIST}')
    MAX_COUNT = 1   # пусть максимальная частота появления числа в массиве равна 1
    NUMBER = USER_LIST[0]   # пусть число, которое появляетя чаще всего равно первому элементу массива
    for i in range(LENGTH-1):
        COUNT = 1   # счетчик частоты появления элемента в массиве
        for j in range(i+1, LENGTH):
            if j > i and USER_LIST[i] == USER_LIST[j]:
                COUNT += 1
            if COUNT > MAX_COUNT:
                NUMBER = USER_LIST[i]
                MAX_COUNT = COUNT
    print(f'Число {NUMBER} встечается в массиве {MAX_COUNT} раз(а)')
except ValueError:
    print('Неверно введено значение длины массива')


