

def int_func():
    while True:
        try:
            print('Введите несколько слов, разделенных пробелами')
            my_str = input()
            find = " "
            if find not in my_str:
                print("Неверный формат")
                continue
            else:
                break
        except Exception as e:
            print("Неверный формат")

    my_list = str(my_str.title())
    return my_list


esc = 0
while esc != 1:
    print(int_func())
    print("Выйти из программы? 0/1")
    esc = int(input())