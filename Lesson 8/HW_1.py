# Шифрование строк с использованием хэш-функций

import hashlib

USER_STRING = input('Введите строку из маленьких латинских букв: ')
str_set = set()     # формирование множества для хранения неповторяющихся подстрок
hash_set = set()    # формирование множества для хранения закодированных подстрок
LENGTH_STR = len(USER_STRING)
for i in range(LENGTH_STR):
    if i == 0:
        LENGTH_STR -= 1
    else:
        LENGTH_STR = len(USER_STRING)
    for k in range(LENGTH_STR, i, -1):
        str_set.add(USER_STRING[i:k])
        hash_set.add(hashlib.sha1(USER_STRING[i:k].encode('utf-8')).hexdigest())
print(f'Массив с подстроками имеет вид: {str_set}')
print(f'Закодированные подстроки имеют вид: {hash_set}')
print(f'Количество различных подстрок в строке {USER_STRING} равно {len(hash_set)}')
