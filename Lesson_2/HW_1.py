# Калькулятор

while True:
    NUMBER_1 = float(input('Введите первое число: '))
    NUMBER_2 = float(input('Введите второе число: '))
    while True:     # проверка правильности введенного знака для выполнения операции
        OPERATION = input('Введите знак операции между числами. Для выхода введите 0: ')
        if OPERATION == '*' or OPERATION == '/' or OPERATION == '+' or OPERATION == '-' or OPERATION == '0':
            break
        else:
            print('Вы ввели неверный знак. Попробуйте ещё раз')
            continue
    if OPERATION == '*':
        MULTIPLICATION = NUMBER_1 * NUMBER_2    # выполнение операции умножения
        print(f'Произведение чисел равно: {MULTIPLICATION}')
    elif OPERATION == '/':
        if NUMBER_2 != 0:
            DIVISION = NUMBER_1/NUMBER_2        # выполнение операции деления
            print(f'Частное чисел равно: {DIVISION}')
        else:
            print('Делить на ноль нельзя!')
    elif OPERATION == '+':      # выполнение операции сложения
        SUM_NUMBER = NUMBER_1 + NUMBER_2
        print(f'Сумма чисел равна: {SUM_NUMBER}')
    elif OPERATION == '-':      # выполнение операции вычитания
        DIFFERENCE = NUMBER_1 - NUMBER_2
        print(f'Разность чисел равна: {DIFFERENCE}')
    else:
        print('Программа завершена')
        break
