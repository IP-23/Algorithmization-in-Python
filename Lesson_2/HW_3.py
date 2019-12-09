# Вывод зеркального числа

NEW_NUMBER = ''     # создание пустой строки для записи в нее зеркального числа
try:
    NUMBER = int(input('Введите целое натуральное число: '))
    LEN = len(str(NUMBER))      # определение длины числа
    while LEN >= 1:
        REMAINS = NUMBER % 10   # остаток от деления на 10
        NEW_NUMBER += str(REMAINS)  # занесение остатка в строку NEW_NUMBER
        NUMBER = NUMBER // 10   # отсечение крайней цифры для формирования нового числа
        LEN = LEN - 1
    print(int(NEW_NUMBER))
except ValueError:
    print('Неверно введено число')
