import utils


a = int(input('Введите 3х значное число: '))

a100 = a // 100
a10 = (a - a100 * 100) // 10
a1 = a % 10

asum = a100 + a10 + a1
amulti = a100 * a10 * a1

print(asum, amulti)

mem_sum = utils.MemorySum()
mem_sum.extend(a, a1, a10, a100, asum, amulti)
print(mem_sum)
