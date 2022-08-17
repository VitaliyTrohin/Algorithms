"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

from random import randint


def value_1(some_list_1):  # O(n^2) Квадратичная
    for i in some_list_1:
        num_min = True
        for j in some_list_1:
            if i > j:
                num_min = False
            if num_min:
                return i


def value_2(some_list_2):  # O(n) Линейная
    min_value = some_list_2[0]
    for i in some_list_2:
        if i < min_value:
            min_value = i
    return min_value


lst_1 = [randint(0, 100) for i in range(20)]
print(lst_1)
print(value_1(lst_1))
print(value_2(lst_1))
