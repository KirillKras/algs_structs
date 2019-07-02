#Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
#и отсортированный массивы.

import random


def merge_sort(lst):
    len_lst = len(lst)
    if len_lst < 2:
        return lst
    lst_left = merge_sort(lst[:len_lst // 2])
    lst_right = merge_sort(lst[len_lst // 2:])

    i = j = 0
    res = []
    while i < len(lst_left) or j < len(lst_right):
        if i >= len(lst_left):
            res.append(lst_right[j])
            j += 1
        elif j >= len(lst_right):
            res.append(lst_left[i])
            i += 1
        elif lst_left[i] < lst_right[j]:
            res.append(lst_left[i])
            i += 1
        else:
            res.append(lst_right[j])
            j += 1
    return res


lst = [round(random.uniform(0, 49), 2) for _ in range(5)]
print(lst)
print(merge_sort(lst))