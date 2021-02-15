from random import randrange

esc = 0
while esc != 1:
    my_list = [randrange(10) for i in range(randrange(50))]
    result_list = [el for el in my_list if my_list.count(el) == 1]
    print(f"Случайный список - {my_list}")
    print(f"Результат - {result_list}")
    print("Выйти из программы? 0/1")
    esc = int(input())