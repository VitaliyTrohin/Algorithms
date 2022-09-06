"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import random
from timeit import timeit


def gnome_sort(some_list, m):
    index = 1
    i = 0
    n = len(some_list)
    while i < n - 1:
        if some_list[i] <= some_list[i + 1]:
            i, index = index, index + 1
        else:
            some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
            i -= 1
            if i < 0:
                i, index = index, index + 1
    return some_list[m]


if __name__ == '__main__':
    m_1 = 10
    m_2 = 100
    m_3 = 1000
    list_1 = list(round(random() * 100) for i in range(2 * m_1 + 1))
    list_2 = list(round(random() * 100) for i in range(2 * m_2 + 1))
    list_3 = list(round(random() * 100) for i in range(2 * m_3 + 1))

    print(gnome_sort(list_1, m_1), timeit('gnome_sort(list_1, m_1)', globals=globals(), number=1000))
    print(gnome_sort(list_2, m_2), timeit('gnome_sort(list_2, m_2)', globals=globals(), number=1000))
    print(gnome_sort(list_3, m_3), timeit('gnome_sort(list_2, m_2)', globals=globals(), number=1000))
