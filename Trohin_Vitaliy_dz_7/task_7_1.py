"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

from random import randint
from timeit import timeit


def bubble_sort(numbers):
    n = 1
    while n < len(numbers):
        for i in range(len(numbers) - n):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        n += 1
    return numbers


def bubble_sort_2(numbers):
    n = 1
    m = 0
    while n < len(numbers):
        for i in range(len(numbers) - n):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                m += 1
        if m == 0:
            break
        n += 1
    return numbers


list_1 = [randint(-100, 100) for _ in range(10)]
print(f'Исходный массив на 10 элементов: \n{list_1}')
print(f'Отсортированный массив: \n{bubble_sort(list_1[:])}')
print(timeit("bubble_sort(list_1[:])", globals=globals(), number=1000))
print(f'Отсортированный массив_2: \n{bubble_sort_2(list_1[:])}')
print(timeit("bubble_sort_2(list_1[:])", globals=globals(), number=1000))
print('\n')

list_2 = [randint(-100, 100) for _ in range(100)]
print(f'Исходный массив на 100 элементов: \n{list_2}')
print(f'Отсортированный массив: \n{bubble_sort(list_2[:])}')
print(timeit("bubble_sort(list_2[:])", globals=globals(), number=1000))
print(f'Отсортированный массив_2: \n{bubble_sort_2(list_2[:])}')
print(timeit("bubble_sort_2(list_2[:])", globals=globals(), number=1000))
print('\n')

list_3 = [randint(-100, 100) for _ in range(1000)]
print(f'Исходный массив на 1000 элементов: \n{list_3}')
print(f'Отсортированный массив: \n{bubble_sort(list_3[:])}')
print(timeit("bubble_sort(list_3[:])", globals=globals(), number=1000))
print(f'Отсортированный массив_2: \n{bubble_sort_2(list_3[:])}')
print(timeit("bubble_sort_2(list_3[:])", globals=globals(), number=1000))

'''
Разница во времени до и после оптимизации с небольшими массивами незначительная. 
При больших массивах лучше использовать сортировку до оптимизации, она быстрее.
'''
