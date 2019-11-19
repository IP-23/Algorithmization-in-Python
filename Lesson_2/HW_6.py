# Угадайка

from random import random
NUMBER = int(random()*100)  # вычисление случайного числа от 0 до 100
i = 1   # счетчик попыток
while i <= 10:
    try:
        USER_NUMBER = int(input('Угадайте число: '))
        if i < 10:
            if USER_NUMBER > NUMBER:
                print(f'Загаданное число меньше. Вы можете попробовать еще {10-i} раз')
            elif USER_NUMBER < NUMBER:
                print(f'Загаданное число больше. Вы можете попробовать еще {10-i} раз')
            else:
                print('Поздравляю! Вы угадали')
                break
        else:
            print(f'К сожалению вы не угадали. Загаданное число равно {NUMBER}')
        i += 1
        continue
    except ValueError:
        print('Неверный формат числа. Попробуйте ещё раз')
        continue
