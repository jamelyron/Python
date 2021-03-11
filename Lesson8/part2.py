
class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_func():
    try:
        print("Введите делимое")
        a = int(input())
        print("Введите делитель")
        b = int(input())
        if b == 0:
            raise ZeroError("Делить на '0' нельзя!")
        else:
            c = a / b
            return c

    except ZeroError as e:
        return "Делить на '0' нельзя!"
    except ValueError:
        return "Неверный формат"


esc = 0
while esc != 1:
    print(my_func())
    print("Выйти из программы? 0/1")
    esc = int(input())
