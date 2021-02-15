from functools import reduce


def my_func(el, elem):
    return el * elem


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f"список чисел - {my_list}")
print(f"результат - {reduce(my_func, my_list)}")
