# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for y in range(M):
        n = int(random() * 200)
        b.append(n)
        print('{0}'.format(n), end=' ')
    a.append(b)
    print()

max = -1
for y in range(M):
    min = 200
    for i in range(N):
        if a[i][y] < min:
            min = a[i][y]
    if min > max:
        max = min
print('\nМаксимальный среди минимальных: ', max)
