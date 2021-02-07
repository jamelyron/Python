my_list = [7, 5, 3, 3, 2]
esc = 0
while esc != 1:
    while True:
        try:
            print('Введите значение рейтинга')
            my_list.append(int(input()))
            break
        except Exception as e:
            print("Неверный формат")
    my_list = sorted(my_list, reverse=True)
    print("рейтинг на данный момент:", ', '.join(map(str, my_list)))
    print("Выйти из программы? 0/1")
    esc = int(input())