# 4 Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.

# *Пример:*

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите степень: '))
with open('fileTask4.txt', 'w') as data:
    data.write('')

for i in range(k+1):
    n = random.randint(0, 101)
    m = random.randint(0, 101)
    if k != 1 and k != 0:
        with open('fileTask4.txt', 'a') as data:
            data.write(f'{n}x**{k} + ')
    elif k == 1:
        with open('fileTask4.txt', 'a') as data:
            data.write(f'{n}x + {m} = 0 ')
    k -= 1
