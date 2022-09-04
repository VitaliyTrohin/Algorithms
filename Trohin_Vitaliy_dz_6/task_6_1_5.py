# Задание 4 из урока 5

from memory_profiler import profile
import json

some_dict_1 = {}


@profile
def append_dict_1():
    for i in range(10000):
        some_dict_1[i] = i
    return some_dict_1


new_dict_1 = append_dict_1()


@profile
def append_dict_2():
    some_dict_2 = {}
    for i in range(100000):
        some_dict_2[i] = i + 1
    with open("dict_file.json", "w") as dict_file:
        json.dump(some_dict_2, dict_file)
    del some_dict_2


new_dict_2 = append_dict_2()

# Сохранение словаря в файл json позволило уменьшить объём потребляемой памяти.
