# Отсортируйте по возрастанию методом слияния одномерный вещ. массив, заданный случ. числами на промежутке [0; 50).

import timeit
import random


def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list


ORIG_LIST = [round(random.random()*50, 2) for i in range(15)]
print(f'Исходный массив имеет вид: {ORIG_LIST}')
print(f'Отсортированный массив имеет вид: {merge_sort(ORIG_LIST)}')

# Замеры
print(timeit.timeit("merge_sort(ORIG_LIST)", setup="from __main__ import merge_sort, ORIG_LIST", number=10))
