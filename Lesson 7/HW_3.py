# Поиск медианы в массиве

from random import randint


def find_min(user_list):    # функция для поиска минимального элемента массива
    minimum = user_list[0]      # пусть минимальным элементом будет элемент с индексом 0
    for i in range(len(user_list)):
        if user_list[i] <= minimum:
            minimum = user_list[i]
    return minimum


def find_max(user_list):    # функция для поиска максимального элемента массива
    maximum = user_list[0]      # пусть максимальным элементом будет элемент с индексом 0
    for i in range(len(user_list)):
        if user_list[i] >= maximum:
            maximum = user_list[i]
    return maximum


USER_NUMBER = int(input('Введите число m для формирования массива: '))
ORIG_LIST = [randint(0, 100) for i in range(2*USER_NUMBER + 1)]     # формирование массива случайных целых чисел
print(f'Исходный массив имеет вид: {ORIG_LIST}')

for i in range(USER_NUMBER):
    LST_MAX = find_max(ORIG_LIST)   # поиск максимального элемента
    ORIG_LIST.remove(LST_MAX)       # удаление максимального элемента из массива
    LST_MIN = find_min(ORIG_LIST)   # поиск минимального элемента
    ORIG_LIST.remove(LST_MIN)       # удаление минимального элемента из массива
print(f'Медиана ряда равна: {ORIG_LIST[0]}')
