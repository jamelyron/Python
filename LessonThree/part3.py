'''решение без позиционных аргументов (мне так понравилось)


def my_func():
    try:
        my_list = []
        i = 0
        while i < 3:
            print(f"Введите {i+1} значение")
            my_list.append(int(input()))
            i += 1
        my_list = sorted(my_list, reverse=True)
        data = my_list[0] + my_list[1]
        return data

    except Exception as e:
        return "Неверный формат"


esc = 0
while esc != 1:
    print(my_func())
    print("Выйти из программы? 0/1")
    esc = int(input())'''


def my_func(*args):
    my_list = []
    for el in args:
        my_list.append(el)
    my_list = sorted(my_list, reverse=True)
    data = my_list[0] + my_list[1]
    return data


esc = 0
while esc != 1:
    print(my_func(int(input("Введите первое число")),
                  int(input("Введите второе число")),
                  int(input("Введите третье число"))))
    print("Выйти из программы? 0/1")
    esc = int(input())
