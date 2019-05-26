'''
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
'''

SYMBOL_START = 32
SYMBOL_STOP = 127
for i in range(SYMBOL_START, SYMBOL_STOP, 10):
    s = ''
    for j in range(10):
        c = i + j
        if c <= SYMBOL_STOP:
            s += f' {c} - {chr(c)} '
    print(s)