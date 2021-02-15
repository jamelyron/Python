from itertools import cycle
from itertools import count


def count_func():
    try:
        print("Введите стартовое число")
        start = int(input())
        print("Введите конечное число")
        stop = int(input())
        for el in count(start):
            if el > stop:
                break
            else:
                print(el)
    except Exception as e:
        print("Неверный формат")


def cycle_func():
    print('Сколько элементов в списке?')
    num = int(input())
    try:
        i = 0
        my_list = []

        while i < num:
            print(f'Введите {i+1} число')
            j = int(input())
            my_list.append(j)
            i += 1
        print(my_list)

        print("Введите число повторений")
        num = int(input())
        i = 0
        data = cycle(my_list)
        while i < num:
            print(next(data))
            i += 1
    except Exception as e:
        print("Неверный формат2")


esc = 0
while esc != 1:
    print("Генератор чисел")
    count_func()
    print("Повторение элементов списка")
    cycle_func()
    print("Выйти из программы? 0/1")
    esc = input()
