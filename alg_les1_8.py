'''
Определить, является ли год, который ввел пользователь, високосным или не високосным.
'''


y = int(input('Введите год:'))

if y % 400 == 0:
    print('Високосный')
elif y % 100 == 0:
    print('Не високосный')
elif y % 4 == 0:
    print('Високосный')
else:
    print('Не високосный')
