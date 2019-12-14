# Счетчик четных и нечетных цифр в веденном числе

ODD = 0     # счетчик четных чисел
EVEN = 0    # счетчик нечетных чисел
try:
    NUMBER = int(input('Введите любое целое натуральное число: '))
    LEN = len(str(NUMBER))      # определение длины введенного числа
    while LEN >= 1:
        REMAINS = NUMBER % 10   # отсечение крайней цифры числа для проверки ее на четность
        if REMAINS % 2 == 0 or REMAINS == 0:
            EVEN += 1
        else:
            ODD += 1
        NUMBER = NUMBER // 10   # отсечение крайней цифры для формирования нового числа
        LEN = LEN - 1
except ValueError:
    print('Неверно введено число')

print(f'В числе {EVEN} четных и {ODD} нечетных чисел')
