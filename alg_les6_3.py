import utils




n = int(input('Введите натуральное число: '))
s1 = 0
s2 = n * (n + 1) / 2
for i in range(1, n+1):
    s1 += i

if s1 == s2:
    print(f'{s1} = {int(s2)}')

mem_size = utils.MemorySum()
mem_size.extend(n, s1, s2, i)
print(mem_size)