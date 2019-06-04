'''
Определить, какое число в массиве встречается чаще всего.
'''

import random

COUNT = 10
MIN_VALUE = 1
MAX_VALUE = 10

l = [random.randint(MIN_VALUE, MAX_VALUE) for i in range(COUNT)]
print(l)

d = {}
max_count = 1
count_index = 0
for i, v in enumerate(l):
    if v in d:
        d[v] += 1
        if d[v] > max_count:
            max_count = d[v]
            count_index = i
    else:
        d[v] = 1

print(f'Наиболее часто встречающийся элемент массива {l[count_index]}')
