# Поиск в массиве максимального отрицательного числа

from random import randint
try:
    LENGTH = int(input('Введите длину массива, который необходимо сформировать: '))
    USER_LIST = [randint(-10, 10) for i in range(LENGTH)]  # формирование массива с случ. элементами от -10 до 10
    MAX_NEGATIVE = 0
    print(f'Исходный массив имеет вид: {USER_LIST}')
    for i in range(LENGTH):     # цикл для поиска минимального числа в массиве
        if USER_LIST[i] < MAX_NEGATIVE:
            MAX_NEGATIVE = USER_LIST[i]
    for i in range(LENGTH):     # цикл для поиска максимального из отрицательных чисел
        if (USER_LIST[i]) < 0 and (USER_LIST[i] > MAX_NEGATIVE):
            MAX_NEGATIVE = USER_LIST[i]
    print(f'Максимальное из отрицательных чисел в массиве равно {MAX_NEGATIVE}.'
          f'\nЕго позиция в массиве: {USER_LIST.index(MAX_NEGATIVE)} (индексация начинается с 0)')
except ValueError:
    print('Неверно введено значение длины массива')
