# Генератор случайного целого числа, случайного вещественного числа, буквы латинского алфавита

from random import random
print('Генератор случайных целых чисел')
LEFT = int(input('Введите минимальную границу: '))
RIGHT = int(input('Введите максимальную границу: '))
if LEFT > 0:
    RANDOM_NUMBER = int(random()*(RIGHT - LEFT) + LEFT)
else:
    RANDOM_NUMBER = int(random() * (abs(LEFT) + RIGHT) + LEFT)
print(RANDOM_NUMBER)

print('Генератор случайных вещественных чисел')
LEFT = float(input('Введите минимальную границу: '))
RIGHT = float(input('Введите максимальную границу: '))
if LEFT > 0:
    RANDOM_NUMBER = float(random()*(RIGHT - LEFT) + LEFT)
else:
    RANDOM_NUMBER = float(random() * (abs(LEFT) + RIGHT) + LEFT)
print(round(RANDOM_NUMBER, 2))

print('Генератор случайных латинских букв')
LEFT = ord(input('Введите минимальную границу: '))
RIGHT = ord(input('Введите максимальную границу: '))
if ord('a') <= LEFT and RIGHT <= ord('z'):
    RANDOM_LETTER = chr(int(random()*(RIGHT - LEFT) + LEFT))
    print(RANDOM_LETTER)
else:
    print('Вы ввели неверные символы')
