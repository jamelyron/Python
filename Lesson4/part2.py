
from random import randrange

esc = 0
while esc != 1:
    my_list = [randrange(100) for i in range(randrange(14))]
    result_list = [el for i, el in enumerate(my_list) if my_list[i - 1] < my_list[i] and i != 0]
    print(f"Случайный список - {my_list}")
    print(f"Результат - {result_list}")
    print("Выйти из программы? 0/1")
    esc = int(input())