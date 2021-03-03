
class Cell:
    def __init__(self, group_1, group_2):
        self.group_1 = group_1
        self.group_2 = group_2

    def __str__(self):
        return f'Изначальные ячейки 1й клетки - {self.group_1 * "*"} \n' \
               f'Изначальные ячейки 2й клетки - {self.group_2 * "*"} \n'

    def __add__(self):
        return f'Сложение клеток - {(self.group_1 + self.group_2) * "*"}'

    def __sub__(self):
        if self.group_1 > self.group_2:
            return f'Вычитание клеток - {(self.group_1 - self.group_2) * "*"}'
        else:
            return f'Нельза вычесть! ячеек не останется!'

    def __mul__(self):
        return f'Умножение клеток - {(self.group_1 * self.group_2) * "*"}'

    def __truediv__(self):
        return f'Деление клеток - {round(self.group_1 // self.group_2) * "*"}'

    def make_order(self, rows):
        row_1 = ''
        row_2 = ''
        for i in range(int(self.group_1 / rows)):
            row_1 += f'{"*" * rows} \n'
        row_1 += f'{"*" * (self.group_1 % rows)}'
        for j in range(int(self.group_2 / rows)):
            row_2 += f'{"*" * rows} \n'
        row_2 += f'{"*" * (self.group_2 % rows)}'

        return f'Первые ячейки клеток по рядам -\n{row_1}\n' \
               f'Вторые ячейки клеток по рядам -\n{row_2}'


print('Сколько ячеек в первой клетке?')
first = int(input())
print('Сколько ячеек во второй клетке?')
second = int(input())
cell = Cell(first, second)
print(cell.__str__())
print(cell.__add__())
print(cell.__sub__())
print(cell.__mul__())
print(cell.__truediv__())
print("Сколько клеток в ряду?")
rows = int(input())
print(cell.make_order(rows))
