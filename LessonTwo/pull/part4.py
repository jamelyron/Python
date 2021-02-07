esc = 0
while esc != 1:
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
    my_list = my_str.split(" ")
    for num, val in enumerate(my_list, 1):
        print(str(num) + '-ое слово ' + str(val[0:10]))

    print("Выйти из программы? 0/1")
    esc = int(input())