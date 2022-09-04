# Задание 1 из 4-го урока

from memory_profiler import profile


@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
def func_2(nums):
    new_list = filter(lambda x: x % 2 == 0, nums)
    return new_list


num = tuple(range(100000))
func_1(num)
func_2(num)

# При использовании функции filter используется значительно меньше памяти.
