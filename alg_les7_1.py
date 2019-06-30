#Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
#заданный случайными числами на промежутке [-100; 100). Выведите на экран
#исходный и отсортированный массивы.


import random


def sort_to_min(lst):
    list_len = len(lst)
    for i in range(list_len-1):
        for j in range(list_len-i-1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


lst = [random.randint(-100, 99) for _ in range(10)]
print(lst)
print(sort_to_min(lst))