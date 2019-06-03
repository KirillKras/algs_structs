'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random

COUNT = 10
MIN_VALUE = 1
MAX_VALUE = 100

l = [random.randint(MIN_VALUE, MAX_VALUE) for i in range(COUNT)]
print(l)

min_i = max_i = 0
min_v = max_v = l[0]

for i, v in enumerate(l):
    if v > max_v:
        max_i = i
        max_v = v
    if v < min_v:
        min_i = i
        min_v = v

l[min_i], l[max_i] = max_v, min_v
print(l)