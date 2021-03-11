from datetime import date


class Data:

    def __init__(self, data):
        self.data = data

    @classmethod
    def unpack(cls, data):
        my_list = [int(i) for i in data.split('-')]
        return f'Ваша дата {my_list[0]} день {my_list[1]} месяца {my_list[2]} года'

    @staticmethod
    def validator(data):
        try:
            my_list = [int(i) for i in data.split('-')]
            date(my_list[0], my_list[1], my_list[2])
            return f'Дата указана верно!'
        except Exception as e:
            return


data = Data


def enter():
    while True:
        try:
            print('Введите дату в формате "дд-мм-гг"')
            a = input()
            if data.validator(a) == 'Дата указана верно!':
                print(data.validator(a))
                return a
            else:
                print('Неверный формат')
        except Exception:
            return


print(data.unpack(enter()))
