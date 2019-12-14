# Реализация алгоритма Хаффмана

from collections import deque, Counter


def haf_algorithm(user_string):
    count = Counter(user_string)   # подсчет уникальных символов
    # Сортировка по неубыванию количества элементов строки
    non_decreasing_sorting = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(non_decreasing_sorting) != 1:
        while len(non_decreasing_sorting) > 1:
            # Определим вес объединенных крайних левых элементов
            cumulative_freq = non_decreasing_sorting[0][1] + non_decreasing_sorting[1][1]
            merged_el = {0: non_decreasing_sorting.popleft()[0],    # объединенный элемент
                         1: non_decreasing_sorting.popleft()[0]}
            for i, _count in enumerate(non_decreasing_sorting):
                if cumulative_freq > _count[1]:
                    continue
                else:
                    # Вставка объединенного корневого элемента
                    non_decreasing_sorting.insert(i, (merged_el, cumulative_freq))
                    break
            else:
                # Добавление объединенного корневого элемента после завершения цикла
                non_decreasing_sorting.append((merged_el, cumulative_freq))
    else:
        # Приравниваем значение 0 к одному повторяющемуся символу
        cumulative_freq = non_decreasing_sorting[0][1]
        merged_el = {0: non_decreasing_sorting.popleft()[0], 1: None}
        # Получение бинарного дерева в виде словаря
        non_decreasing_sorting.append((merged_el, cumulative_freq))
    return non_decreasing_sorting[0][0]


res_code = dict()


def haf_code(tree, path=''):    # функция заполняет кодовую таблицу (символ: его код)
    # Если элемент не словарь, значит мы достигли самого символа
    # и заносим его, а также его код в словарь (кодовую таблицу).
    if not isinstance(tree, dict):
        res_code[tree] = path
    # Если элемент словарь, рекурсивно спускаемся вниз
    # по первому и второму значению (левая и правая ветви).
    else:
        haf_code(tree[0], path=f'{path}0')
        haf_code(tree[1], path=f'{path}1')


USER_STRING = "ship sheep sheet"
haf_code(haf_algorithm(USER_STRING))

# Вывод закодированных букв и символов поэлементно
for i in USER_STRING:
    print(res_code[i], end=' ')
print()
