# Прибыль фирм за 4 квартала. Вычисление средней прибыли

from collections import namedtuple

LST_FIRM = []   # список фирм
INCOME = []     # список прибылей фирм
NUMBER = int(input('Введите количство фирм для рассмотрения: '))

for i in range(NUMBER):
    Firm = namedtuple('Firm', 'name first_quarter second_quarter third_quarter fourth_quarter')
    RES_FIRM = Firm(
        name=input('\nВведите название предприятия: '),
        first_quarter=float(input('Введите прибыль за первый квартал: ')),
        second_quarter=float(input('Введите прибыль за второй квартал: ')),
        third_quarter=float(input('Введите прибыль за третий квартал: ')),
        fourth_quarter=float(input('Введите прибыль за четвертый квартал: '))
    )
    INCOME_FIRM = RES_FIRM.first_quarter + RES_FIRM.second_quarter + RES_FIRM.third_quarter + RES_FIRM.fourth_quarter
    INCOME.append(INCOME_FIRM)
    LST_FIRM.append(RES_FIRM)
    print(f'Прибыль фирмы {RES_FIRM.name}: {INCOME_FIRM}')

AVR_INCOME = sum(INCOME)/NUMBER   # вычисление среднегодовой прибыли
print(f'\nСреднегодовая прибыль рассмотренных фирм составляет: {AVR_INCOME}')
print('\nФирмы, имеющие прибыль выше среднего: ')
for i in range(NUMBER):
    if INCOME[i] >= AVR_INCOME:
        print(LST_FIRM[i].name)

print('\nФирмы, имеющие прибыль ниже среднего: ')
for i in range(NUMBER):
    if INCOME[i] < AVR_INCOME:
        print(LST_FIRM[i].name)
