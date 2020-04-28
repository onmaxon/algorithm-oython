# 3.7.4 (default, Jul  9 2019, 16:32:37)
# [GCC 9.1.1 20190503 (Red Hat 9.1.1-1)] x86_64

import sys

number = int(input('Введите: '))
num = 0
while number > 0:
    num = num * 10 + number % 10
    number = number // 10
print(num)

sum_size = 0
sum_size += sys.getsizeof(num)

print('\nПеременные занимают {0} байт'.format(sum_size))

# Переменные занимают 28 байт

