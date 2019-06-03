'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''
MIN_RANGE = 2
MAX_RANGE = 99

numbers = [i for i in range(MIN_RANGE,MAX_RANGE+1)]

d = {i: 0 for i in range(2,9+1)}


for i in numbers:
    for k in d.keys():
        if i % k == 0:
            d[k] += 1

print(d)