# 2 Задайте натуральное число N.
# Напишите программу, которая составит список простых
# множителей числа N.
n = int(input('Введите натуральное число: '))
# list = []

def mn(m):
    mnog = []
    d = 2
    while d * d <= m:
        if m % d == 0:
            mnog.append(d)
            m //= d
        else:
            d += 1
    if m > 1:
        mnog.append(m)
    return mnog

list = mn(n)
print(list)
