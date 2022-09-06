"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import random
from timeit import timeit


def my_median(obj, m):
    my_list = obj[:]
    while m > 0:
        my_list.pop(my_list.index(max(my_list)))
        m -= 1
    return my_list.pop(my_list.index(max(my_list)))


if __name__ == '__main__':
    m_1 = 10
    m_2 = 100
    m_3 = 1000
    list_1 = list(round(random() * 100) for i in range(2 * m_1 + 1))
    list_2 = list(round(random() * 100) for i in range(2 * m_2 + 1))
    list_3 = list(round(random() * 100) for i in range(2 * m_3 + 1))

    print(my_median(list_1, m_1), timeit('my_median(list_1, m_1)', globals=globals(), number=100))
    print(my_median(list_2, m_2), timeit('my_median(list_2, m_2)', globals=globals(), number=100))
    print(my_median(list_3, m_3), timeit('my_median(list_3, m_3)', globals=globals(), number=100))
