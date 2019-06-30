#Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
#Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
#в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random
import math


def my_min(lst):
    min_value = math.inf
    min_idx = 0
    for i, value in enumerate(lst):
        if value < min_value:
            min_value = value
            min_idx = i
    return min_idx, min_value


def my_max(lst):
    max_value = 1
    max_idx = 0
    for i, value in enumerate(lst):
        if value > max_value:
            max_value = value
            max_idx = i
    return max_idx, max_value


def get_median(lst):
    lst_left = lst[:m]
    median = lst[m]
    lst_right = lst[m + 1:]

    found = False
    while not found:
        max_idx, max_value = my_max(lst_left)
        min_idx, min_value = my_min(lst_right)
        if max_value <= median <= min_value:
            found = True
        elif max_value > median:
            median, lst_left[max_idx] = lst_left[max_idx], median
        elif median > min_value:
            median, lst_right[min_idx] = lst_right[min_idx], median
    return median


m = int(input('Введите m: '))

lst = [random.randint(1, 100) for _ in range(2*m+1)]
print(lst)
print(get_median(lst))


