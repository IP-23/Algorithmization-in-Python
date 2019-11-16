# Определение позиции введенных букв и количества букв между ними

LETTER_1 = input('Ввведите любую букву латинского алфавита: ')
LETTER_2 = input('Ввведите ещё какую-нибудь букву латинского алфавита: ')
POS_A = ord('a')    # определение позиции буквы 'a'
POS_LETTER_1 = ord(LETTER_1.lower()) - POS_A + 1    # определение позиции первой буквы
POS_LETTER_2 = ord(LETTER_2.lower()) - POS_A + 1    # определение позиции второй буквы
if POS_LETTER_2 > POS_LETTER_1:     # определение количества букв между введенными буквами
    DISTANCE = POS_LETTER_2 - POS_LETTER_1 - 1
else:
    DISTANCE = POS_LETTER_1 - POS_LETTER_2 - 1

print(f'Позиция буквы {LETTER_1} в алфавите {POS_LETTER_1}'
      f'\nПозиция буквы {LETTER_2} в алфавите {POS_LETTER_2}'
      f'\nМежду ними {DISTANCE} букв(ы)')
