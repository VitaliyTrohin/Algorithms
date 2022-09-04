from memory_profiler import memory_usage
from numpy import array


def decor(func_1):
    def wrapper(*args):
        m1 = memory_usage()
        print(m1)
        res = func_1(args[0])
        m2 = memory_usage()
        print(m2)
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


@decor
def func_2(nums):
    my_list = []
    for k, v in enumerate(nums):
        if v % 2 == 0:
            my_list.append(k)
    return my_list


# my_arr = list(range(100000))
my_arr = array(list(range(100000)))
result, delta = func_2(my_arr)

print(delta)

# C помощью модуля array память расходуется меньше
