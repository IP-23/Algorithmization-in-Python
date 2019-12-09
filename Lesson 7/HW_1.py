# Пузырьковая сортировка

import timeit
from random import randint


def bubble_sort(orig_list):
    n = 1
    k = 0
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                k += 1
#        if k == 0:
#           break
        n += 1
    return orig_list


ORIG_LIST = [randint(1, 100) for i in range(25)]
print(ORIG_LIST)
print(bubble_sort(ORIG_LIST))

# Замеры
print(timeit.timeit('bubble_sort(ORIG_LIST)', setup='from __main__ import bubble_sort, ORIG_LIST', number=100000))

