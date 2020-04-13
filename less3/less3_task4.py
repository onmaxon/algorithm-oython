# Определить, какое число в массиве встречается чаще всего.

from random import random

N = int(input('Введите количество цифр в массиве: '))
array = [0] * N
for i in range(N):
    array[i] = int(random() * 20)
print(array)

num = array[0]
max_rep = 1
for i in range(N - 1):
    rep = 1
    for k in range(i + 1, N):
        if array[i] == array[k]:
            rep += 1
    if rep > max_rep:
        max_rep = rep
        num = array[i]

if max_rep > 1:
    print('{0} раз(а) встречается число {1}'.format(max_rep, num))
else:
    print('Все элементы уникальны')
