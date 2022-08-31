"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

some_dict = {}
ord_dict = OrderedDict()


def append_dict():
    for i in range(10000):
        some_dict[i] = i


def append_ord_dict():
    for i in range(10000):
        ord_dict[i] = i


print(f'append_dict: {timeit(append_dict, number=1000)}')
print(f'append_ord_dict: {timeit(append_ord_dict, number=1000)}')


def popitem_dict():
    simple_dict_copy = some_dict.copy()
    for k in range(1000):
        simple_dict_copy.popitem()


def popitem_ord_dict():
    ord_dict_copy = ord_dict.copy()
    for k in range(1000):
        ord_dict_copy.popitem()


print(f'pop dict: {timeit(popitem_dict, number=1000)}')
print(f'pop ord dict: {timeit(popitem_ord_dict, number=1000)}')

# Нет смысла использовать OrderedDict, т.к. по скорости он медленее словаря.
