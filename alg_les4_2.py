import cProfile

def eratosfen(index):

    n = index * 100
    count = 0
    sieve = [i for i in range(n)]
    sieve[1] = 0
    count = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            count += 1
            if count == index:
                return sieve[i]
            while j < n:
                sieve[j] = 0
                j += i

'''
index = 500
100 loops, best of 3: 11 msec per loop

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.023    0.023 <string>:1(<module>)
        1    0.019    0.019    0.022    0.022 alg_les4_2.py:3(eratosfen)
        1    0.004    0.004    0.004    0.004 alg_les4_2.py:7(<listcomp>)
        1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''


def prime(index):
    i = 2
    count = 0
    result = None
    while True:
        flag = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            count += 1
            result = i
        if count == index:
            return result
        i += 1

'''
index = 500

100 loops, best of 3: 23.4 msec per loop

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.040    0.040 <string>:1(<module>)
        1    0.040    0.040    0.040    0.040 alg_les4_2.py:29(prime)
        1    0.000    0.000    0.040    0.040 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''

#cProfile.run('prime(500)')