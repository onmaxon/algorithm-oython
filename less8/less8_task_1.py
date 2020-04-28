# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

import hashlib


def count_subs(string):
    new_list = []
    move = 1
    while move < len(string):
        for i in range(0, len(string), 1):
            tmp = hashlib.sha512(string[i:i + move].encode('utf-8')).hexdigest()
            new_list.append(tmp)
        move += 1
    return len(set(new_list))


a = input('Введите строку: ')
print('Число подстрок в строке: {0}'.format(count_subs(a)))
