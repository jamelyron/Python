def my_func (x, y):
    i = 1
    a = x
    while i < y:
        x = x * a
        i += 1
    result = 1 / x
    return result


esc = 0
while esc != 1:
    while True:
        try:
            print('Введите число X')
            x = (int(input()))
            print('Введите отрицательную степень')
            y = (int(input()))
            break
        except Exception as e:
            print("Неверный формат")

    print(f"{x} в степени -{y} = ", my_func(x, y))
    print("Выйти из программы? 0/1")
    esc = int(input())