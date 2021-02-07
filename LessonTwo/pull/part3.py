low, high = 1, 12
esc = 0
while esc != 1:
    while True:
        try:
            print('Введите месяц')
            month = int(input())
            if month < low or month > high:
                print('Введите от 1 до 12')
                continue
            else:
                break
        except Exception as e:
            print("Неверный формат")

    month_list = [[12, 1, 2], [3, 4, 5], [6,7,8], [9,10,11]]
    ear_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
    for el in month_list:
        for elem in el:
            if month == elem:
                print(ear_dict.get(month_list.index(el) + 1))
    print("Выйти из программы? 0/1")
    esc = int(input())
