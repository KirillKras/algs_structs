
from collections import deque


HEX = '0123456789ABCDEF'


def add_zero(a, b):
    la = len(a)
    lb = len(b)

    if la < lb:
        a.extendleft('0' for _ in range(lb - la))
    else:
        b.extendleft('0' for _ in range(la - lb))
    return a, b

def sum(x, y, rotate=False):
    pos_x = HEX.index(x)
    pos_y = HEX.index(y)

    x_hex = deque([None for _ in range(16)])
    x_hex[pos_x] = True

    x_hex.rotate(pos_y + rotate)
    pos_res = x_hex.index(True)
    if pos_res < pos_x:
        return ['1', HEX[pos_res]]
    else:
        return [HEX[pos_res], ]

a_str = input('Введите первое HEX число: ')
b_str = input('Введите второе HEX число: ')

a = deque(a_str)
b = deque(b_str)

a, b = add_zero(a, b)


rotate = False

result = deque()

while a:
    x = a.pop()
    y = b.pop()
    result_sum = sum(x, y, rotate)
    rotate = True if len(result_sum) == 2 else False
    result.appendleft(result_sum.pop())

result_sum.extend(result)

print(f' {a_str} + {b_str} = {result_sum}')