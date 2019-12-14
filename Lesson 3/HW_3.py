# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

from random import randint
try:
    LENGTH = int(input('Введите длину массива, который необходимо сформировать: '))
    USER_LIST = [randint(0, 100) for i in range(LENGTH)]    # формирование массива с случ. элементами от 0 до 5
    print(f'Исходный массив имеет вид: {USER_LIST}')
    # Пусть и max, и min лементы равны первому элементу массива
    MINIMUM, MAXIMUM = USER_LIST[0], USER_LIST[0]
    for i in range(LENGTH):     # поиск max и min элементов массива
        if USER_LIST[i] > MAXIMUM:
            MAXIMUM = USER_LIST[i]
        elif USER_LIST[i] < MINIMUM:
            MINIMUM = USER_LIST[i]
    IND_MIN = USER_LIST.index(MINIMUM)  # поиск индекса min элемента
    IND_MAX = USER_LIST.index(MAXIMUM)  # поиск индекса max элемента
    USER_LIST[IND_MIN], USER_LIST[IND_MAX] = USER_LIST[IND_MAX], USER_LIST[IND_MIN]
    print(f'Новый массив имеет вид: {USER_LIST}')
except ValueError:
    print('Неверно введено значение длины массива')
