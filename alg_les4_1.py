'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

import cProfile

START_NUM = 2
END_NUM = 100000
START_DIV = 2
END_DIV = 9

def variant1():
    result = []
    numbers = [i for i in range(START_NUM,END_NUM + 1)]
    d = {i: 0 for i in range(START_DIV, END_DIV + 1)}
    for i in numbers:
        for k in d.keys():
            if i % k == 0:
                d[k] += 1
    for i, item in d.items():
        result.append(f'Числу {i} кратно {item} чисел')
'''
END_NUM = 100000

100 loops, best of 3: 62.9 msec per loop

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    0.122    0.122 <string>:1(<module>)
        1    0.101    0.101    0.119    0.119 alg_les4_1.py:12(variant1)
        1    0.007    0.007    0.007    0.007 alg_les4_1.py:14(<listcomp>)
        1    0.000    0.000    0.000    0.000 alg_les4_1.py:15(<dictcomp>)
        1    0.000    0.000    0.122    0.122 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
    99999    0.010    0.000    0.010    0.000 {method 'keys' of 'dict' objects}
'''


def variant2():
    result = []
    for i in range(START_DIV, END_DIV + 1):
        frequency = 0
        for j in range(START_NUM, END_NUM + 1):
            if j % i == 0:
                frequency += 1
        result.append(f'Числу {i} кратно {frequency} чисел')
'''
END_NUM = 100000

100 loops, best of 3: 49 msec per loop

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.071    0.071 <string>:1(<module>)
        1    0.071    0.071    0.071    0.071 alg_les4_1.py:40(variant2)
        1    0.000    0.000    0.071    0.071 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

def variant3():
    result = []
    frequency = [0] * (END_DIV - START_DIV + 1)
    for i in range(START_NUM, END_NUM + 1):
        for j in range(START_DIV, END_DIV + 1):
            if i % j == 0:
                frequency[j - START_DIV] += 1
    for i, item in enumerate(frequency, start=START_DIV):
        result.append(f'Числу {i} кратно {item} чисел')
'''
END_NUM = 100000

100 loops, best of 3: 77.4 msec per loop

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.132    0.132 <string>:1(<module>)
        1    0.132    0.132    0.132    0.132 alg_les4_1.py:61(variant3)
        1    0.000    0.000    0.132    0.132 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

cProfile.run('variant3()')

#Лучший по скорости и простоте алгоритм 2, затем 1, самый не оптимальный 3