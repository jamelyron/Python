

def my_func():
    try:
        print("Введите делимое")
        a = int(input())
        print("Введите делитель")
        b = int(input())
        c = a / b

    except ZeroDivisionError:
        return "Делить на '0' нельзя!"
    except Exception as e:
        return "Неверный формат"

    return c


esc = 0
while esc != 1:
    print(my_func())
    print("Выйти из программы? 0/1")
    esc = int(input())
