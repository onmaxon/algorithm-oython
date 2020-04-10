# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input('Введите: '))
even = uneven = 0
while number > 0:
    if number % 2 == 0:
        even += 1
    else:
        uneven += 1
    number = number // 10
print('четных - {0}, нечетных - {1}'.format(even, uneven))
