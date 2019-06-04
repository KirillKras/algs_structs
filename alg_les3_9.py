'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

import random
import math

MIN_VALUE = 1
MAX_VALUE = 100
RAW = 4
COLUMN = 5

matrix = [[random.randint(MIN_VALUE, MAX_VALUE) for _ in range(COLUMN)] for _ in range(RAW)]

for line in matrix:
    print(line)

column_min = [math.inf for _ in range(COLUMN)]

for c in range(COLUMN):
    for r in range(RAW):
        if matrix[r][c] < column_min[c]:
            column_min[c] = matrix[r][c]

max_v = 0
for v in column_min:
    if v > max_v:
        max_v = v

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_v}')
