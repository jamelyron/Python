
class Number(Exception):
    def __init__(self, txt):
        self.txt = txt


print('Для завершения программы введите <stop>')


def enter():
    my_list = []
    i = 1
    while True:
        print(f'Введите {i} значение списка')
        i += 1
        data = input()
        if data.lower() == 'stop':
           return my_list
        else:
            try:
                if data.isnumeric():
                    my_list.append(int(data))
                    print(f'Список на данный момент - {my_list}')
                else:
                    i -= 1
                    raise Number("Err")
            except Number as e:
                print(f"Неверный формат! Введите число! \nИли\nДля завершения программы введите <stop>")


print(f'Итоговый список - {enter()}')
