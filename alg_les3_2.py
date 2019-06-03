'''
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
(индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
'''

import random

COUNT = 10
MIN_VALUE = 1
MAX_VALUE = 100

l = [random.randint(MIN_VALUE, MAX_VALUE) for i in range(COUNT)]
print(l)

res = []

for i, v in enumerate(l):
    if v % 2 == 0:
        res.append(i)
print(res)