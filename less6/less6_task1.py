import sys


# 3.7.4 (default, Jul  9 2019, 16:32:37)
# [GCC 9.1.1 20190503 (Red Hat 9.1.1-1)] x86_64

print('Вывод кода и символа таблицы ASCII\n')

sum_size = 0

for i in range(32, 128):
    sum_size += sys.getsizeof(i)
    print('{0}-{1}'.format(i, chr(i)), end=' ')
    if i % 10 == 0:
        print()

print('\nПеременные занимают {0} байт'.format(sum_size))

# Переменные занимают 2688 байт
