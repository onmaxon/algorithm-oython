# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random

N = 15
array = [0] * N
for i in range(N):
    array[i] = int(random() * 100)
print('\nМассив до изменений:\n', array)

min = min(array)
max = max(array)
imin = array.index(min)
imax = array.index(max)

print('Минимальный элемент - arr[{0}] = {1}\nМаксимальный элемент - arr[{2}] = {3}'.format(imin+1, min, imax+1, max))
print('Меняем местами --->')
array[imin], array[imax] = array[imax], array[imin]
print('Готово:\n', array)
