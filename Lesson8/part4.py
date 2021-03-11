from collections import Counter


class Warehouse:
    def __init__(self, stuff_dict: dict):
        self.stuff_dict = stuff_dict

    def item_in_warehouse(self):
        any_list = []
        for i, j in self.items():
            if j == True:
                any_list.append(i)
        return " ".join(any_list)

    def any_in_warehouse(self):
        any_list = []
        for i, j in self.items():
            any_list.append(str(i))
            any_list.append(str(j))
        return " ".join(any_list)




class OfficeEquipment:

    def __init__(self, model, price, quantity):
        self.model = model
        self.price = price
        self.quantity = quantity
        self.office_data = {'Модель' : model, 'Цена': price, 'Кол-во': quantity}

    @classmethod
    def inputing(cls):
        try:
            print('Введите модель')
            model = input()
            print('Введите цену')
            price = int(input())
            print('Введите количество')
            quantity = int(input())
            data = {'Модель': model, 'Цена': price, 'Кол-во': quantity}
            return data
        except ValueError:
            return "Неверный формат!"
        except Exception as e:
            return "Неверный формат!"


class Printer(OfficeEquipment):

    @staticmethod
    def whatis():
        printer_dict = dict.fromkeys(['Лазерный', 'Цветной'])
        try:
            print('Принтер лазерный? 1/0')
            a = int(input())
            if a == 1:
                printer_dict['Лазерный'] = True
            else:
                printer_dict['Лазерный'] = False
            print('Принтер цветной? 1/0')
            b = int(input())
            if b == 1:
                printer_dict['Цветной'] = True
            else:
                printer_dict['Цветной'] = False
            return printer_dict
        except ValueError:
            return "Неверный формат!"


class Skan(OfficeEquipment):

    @staticmethod
    def whatis():
        mfu: bool
        size = {1: 'A0', 2: 'A2', 3: 'A4'}
        skan_dict = {}
        try:
            print('Это МФУ или сканер? 1/0')
            a = int(input())
            if a == 1:
                mfu = True
                skan_dict['МФУ'] = mfu
            else:
                skan_dict['Слайд-сканер'] = True
            print(f'Какой формат?\nA0 - Введите 1\nА2 - введите 2\nА4 - Введите 3')
            b = int(input())
            skan_dict[size[b]] = True
            return skan_dict
        except ValueError:
            return "Неверный формат!"


class Xerox(OfficeEquipment):

    @staticmethod
    def whatis():
        try:
            print("Ксерокс аналоговый? 1/0")
            a = int(input())
            xerox_dict = dict([('Аналоговый', None), ("Цветной", None)])
            if a == 1:
                xerox_dict['Аналоговый'] = True
            else:
                xerox_dict['Цифровой'] = True
            print("Ксерокс цветной?  1/0")
            b = int(input())
            if b == 1:
                xerox_dict['Цветной'] = True
            else:
                xerox_dict['Ч/Б'] = True
            return xerox_dict
        except ValueError:
            return 'Неверный формат!'


def what_input():
    print('Какая оргтехника поступила?')
    print('"p" - Принтер')
    print('"s" - Сканер')
    print('"x" - Ксерокс')
    switch = str(str.lower(input()))
    sw = of.inputing()
    try:
        if switch == "p":
            return 'Принтер', sw, p.whatis()
        elif switch == "s":
            return 'Сканер', sw, s.whatis()
        elif switch == "x":
            return 'Ксерокс', sw, x.whatis()
        else:
            print("Неверный формат!")
    except Exception as e:
        return "Неверный формат!"


def what_output(data):
    i = 0
    while i < data[1]['Кол-во']:
        calculate.append(data[0])
        i += 1
    cnt = Counter(calculate)
    print('Принят на склад -', data[0], w.item_in_warehouse(data[2]), w.any_in_warehouse(data[1]))
    print(f'На складе - {dict(cnt)}')
    return dict(cnt), data[0], w.item_in_warehouse(data[2]), w.any_in_warehouse(data[1])


p = Printer
s = Skan
w = Warehouse
x = Xerox
of = OfficeEquipment
calculate = []
end = []
output = []
end_dict = {}
esc = 0

while esc == 0:

    while True:
        try:
            output = what_output(what_input())
            end.append(output[1] + " " + output[2] + " " + output[3])
            end_dict.update(output[0])
            break
        except Exception as e:
            print()

    print('Выйти из программы? 1/0')
    esc = int(input())


print(f'На складе - {end_dict}')
for i in end:
    print(i)
