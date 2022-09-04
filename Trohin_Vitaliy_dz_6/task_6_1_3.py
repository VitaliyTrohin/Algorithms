# Задание 4 из урока 2

from memory_profiler import profile


@profile
def wrapper():
    # result = sum_elements_1(500, n_count=0, sum_elem=0, elem=1, sign=True)
    result = sum_elements_2(500)
    return result


def sum_elements_1(n, n_count=0, sum_elem=0, elem=1, sign=True):
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
    return sum_elements_1(n, n_count, sum_elem, elem, sign)


def sum_elements_2(n):
    i = 1
    sum_elements = 0
    while i <= n:
        sum_elements += (-0.5) ** (i - 1)
        i += 1
    return sum_elements


print(wrapper())

# Цикл расходует меньше памяти чем рекурсия.
