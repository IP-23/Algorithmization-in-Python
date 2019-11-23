# Поиск суммы между наибольшим и наименьшим элементом

from random import randint
try:
    LENGTH = int(input('Введите длину массива, который необходимо сформировать: '))
    USER_LIST = [randint(0, 10) for i in range(LENGTH)]     # формирование массива с случ. элементами от 0 до 10
    print(f'Исходный массив имеет вид: {USER_LIST}')
    MAXIMUM, MINIMUM = USER_LIST[0], USER_LIST[0]  # пусть и max, и min эл-ты равны первому элементу массива
    for i in range(LENGTH):
        if USER_LIST[i] < MINIMUM:
            MINIMUM = USER_LIST[i]
        elif USER_LIST[i] > MAXIMUM:
            MAXIMUM = USER_LIST[i]
    # Поиск минимального индекса среди индекса min эл-та и индекса max эл-та
    IND_MIN = min(USER_LIST.index(MINIMUM), USER_LIST.index(MAXIMUM))
    # Поиск максимального индекса среди индекса min эл-та и индекса max эл-та
    IND_MAX = max(USER_LIST.index(MINIMUM), USER_LIST.index(MAXIMUM))
    SUM = 0
    while IND_MIN < (IND_MAX-1):    # расчет суммы элементов между минимальным и максимальным (или наоборот)
        SUM += USER_LIST[IND_MIN+1]
        IND_MIN += 1
    print(f'Наименьший элемент: {MINIMUM}. \nНаибольший элемент: {MAXIMUM}. \nСумма между ними: {SUM}')
except ValueError:
    print('Неверно введено значение длины массива')
