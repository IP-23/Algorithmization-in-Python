# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
# кратны каждому из чисел в диапазоне от 2 до 9.

NUMBERS = list(range(2, 10))     # массив цифр от 2 до 9
USER_LIST = list(range(2, 100))  # массив чисел от 2 до 99
for i in range(len(NUMBERS)):
    COUNT = 0   # счетчик кратных чисел
    for j in range(len(USER_LIST)):
        if (USER_LIST[j] % NUMBERS[i]) == 0:
            COUNT += 1
        j += 1
    print(f'{COUNT} чисел в диапазоне от 2 до 99 кратны числу {NUMBERS[i]}')
    i += 1
