# Сложение и умножение 16-тиричных чисел

from collections import deque

NUMBERS = '0123456789ABCDEF'        # цифры в 16-тиричной системе счисления

A = list('A2')
B = list('C4F')


# Функция для перевода отдельных символов списка из 16-тиричной СС в 10-тиричную
def get_10_digit_number(number, max_len):
    result = deque()    # список, в который будут размещены переведенные цифры
    for i in range(max_len):
        try:
            digit_for_translation = number[-(i+1)]
            hex_digit = NUMBERS.index(digit_for_translation)   # перевод каждого цифры из 16-тиричн. СС в 10-тиричн.
        except IndexError:
            hex_digit = 0
        result.appendleft(hex_digit)  # формирование списка уже переведенных цифр
    return result


# Функция суммирования 16-тиричных чисел
def sum_hex(a_hex, b_hex):
    a_dec = get_10_digit_number(a_hex, max(len(a_hex), len(b_hex)))
    b_dec = get_10_digit_number(b_hex, max(len(a_hex), len(b_hex)))
    result = deque()    # список, в который будут размещены просуммированные поэлементно цифры
    remain = 0  # остаток
    for i in range(max(len(a_hex), len(b_hex))):
        sum_dec = (a_dec[-(i+1)] + b_dec[-(i+1)] + remain) % 16     # суммирование чисел поэлементно, начиная с конца
        remain = (a_dec[-(i+1)] + b_dec[-(i+1)] + remain) // 16
        result.appendleft(NUMBERS[sum_dec])
    if remain:      # если при последнем суммировании образовался остаток, добавить его в начало результ. списка
        result.appendleft(NUMBERS[remain])
    return list(result)


def mul_hex(a_hex, b_hex):
    a_dec = get_10_digit_number(a_hex, max(len(a_hex), len(b_hex)))
    b_dec = get_10_digit_number(b_hex, max(len(a_hex), len(b_hex)))
    result = []     # список, содержащий промежуточные результаты умножения
    mul_res = '0'   # обнуление итогового результата умножения чисел
    remain = 0      # остаток
    for j in range(max(len(a_hex), len(b_hex))):
        part_result = deque()   # массив, содержащий промежуточный результат умножения, разбитый поэлементно
        for i in range(max(len(a_hex), len(b_hex))):
            mul_dec = (a_dec[-(i+1)] * b_dec[-(j+1)] + remain) % 16
            remain = (a_dec[-(i+1)] * b_dec[-(j+1)] + remain) // 16
            part_result.appendleft(NUMBERS[mul_dec])
        if remain:
            part_result.appendleft(NUMBERS[remain])
        part_result = ''.join(part_result)      # склеивание элементов массива part_result
        part_result = part_result + j*'0'       # добавление в крайний разряд нуля
        result.append(''.join(part_result))     # добавление в массив промежуточных результатов итоговых элементов
    for i in range(len(result)):
        mul_res = sum_hex(mul_res, result[i])   # вычисление итогового результата умножения
    return list(mul_res)


print(f'{A} + {B} = {sum_hex(A, B)}')
print(f'{A} * {B} = {mul_hex(A, B)}')
