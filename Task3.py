# 3 Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.


def cnt(x):
    b = []
    for i in set(x):
        if x.count(i) == 1:
            b.append(i)
    return b


n = int(input('Введите размер последовательности: '))
a = []

for i in range(n):
    n = int(input())
    a.append(n)


b1 = cnt(a)
print(b1)
