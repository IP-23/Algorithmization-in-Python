# Поиск двух минимальных элементов массива

from random import randint


def find_min(user_list):    # функция для поиска минимального элемента массива
    minimum = user_list[0]      # пусть минимальным элементом будет элемент с индексом 0
    for i in range(len(user_list)):
        if user_list[i] <= minimum:
            minimum = user_list[i]
    return minimum


try:
    LENGTH = int(input('Введите длину массива, который необходимо сформировать: '))
    USER_LIST = [randint(-10, 10) for i in range(LENGTH)]   # формирование массива с случайными числами от -10 до 10
    print(f'Исходный массив имеет вид: {USER_LIST}')
    MINIMUM_1 = find_min(USER_LIST)     # поиск минимального элемента в массиве
    USER_LIST.remove(MINIMUM_1)         # удаление минимального элемента из массива
    MINIMUM_2 = find_min(USER_LIST)     # поиск минимального элемента в новом массиве
    print(f'{[MINIMUM_1, MINIMUM_2]} - минимальные числа в исходном массиве')
except ValueError:
    print('Неверно введено значение длины массива')
