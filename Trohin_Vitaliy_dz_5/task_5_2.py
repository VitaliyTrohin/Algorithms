"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""

from collections import defaultdict
from functools import reduce


def number():
    value = input('Введите шестнадцатиричное число: ')
    return list(value.upper())


def sum_number(data):
    return list(hex(reduce(lambda x, y: x + y, [int(''.join(i), 16) for i in data.values()])).upper())[2:]


def multiplication(data):
    return list(hex(reduce(lambda x, y: x * y, [int(''.join(i), 16) for i in data.values()])).upper())[2:]


def main():
    def_data = defaultdict(list)
    def_data['1'] = number()
    def_data['2'] = number()
    symbol = input('ВВедите знак операции +/*: ')
    if symbol == '+':
        return ''.join(sum_number(def_data))
    elif symbol == '*':
        return ''.join(multiplication(def_data))


print(main())
