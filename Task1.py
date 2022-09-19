# 1 Вычислить число π c заданной точностью d
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = input('Задайте точность вычисления числа π: ')
arr = list(d)
b = []
arr.remove('.')
arr.reverse()
astr = int(str(''.join(arr)))
count = -1
pi = 0
for i in range(1, 100000, 2):
    count *= -1
    a = count*(4/i)
    pi += a
pi = int(pi * astr)/astr
print(pi)
