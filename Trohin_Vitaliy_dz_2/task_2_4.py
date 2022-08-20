"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_elements(n, n_count=0, sum_elem=0, elem=1, sign=True):
    n_count += 1
    if sign is True:
        sum_elem += elem
        sign = False
    else:
        sum_elem -= elem
        sign = True
    n -= 1
    if n == 0:
        print(f'Количество элементов - {n_count}, их сумма - {sum_elem}')
        return None
    elem /= 2
    sum_elements(n, n_count, sum_elem, elem, sign)


sum_elements(int(input('Введите количество элементов: ')))
