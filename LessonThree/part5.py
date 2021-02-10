

def my_func():
    esc = False
    my_sum = 0
    while esc == False:
        print("Введите несколько чисел для операции или Q для выхода")
        my_str = input()
        my_str = my_str.lower()
        data = my_str.split(" ")

        for el in range(len(data)):
            if data[el] == 'q':
                esc = True
                break
            else:
                my_sum += int(data[el])

        print(f'Сумма чисел = {my_sum}')
    print('Good bye')


my_func()