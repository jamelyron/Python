class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def calc_coat(self):
        return self.size / 6.5 + 0.5

    def calc_jacket(self):
        return 2 * self.height + 0.3

    @property
    def calculate(self):
        return f'Общая площадь ткани - {round(self.calc_coat() + self.calc_jacket(), 2)}'


class Coat(Clothes):

    def __init__(self, size):
        super().__init__(size, None)
        self.calculate_coat = self.calc_coat()

    def __str__(self):
        return f'Ткани для пальто - {round(self.calculate_coat, 2)} м2'


class Jacket(Clothes):

    def __init__(self, height):
        super().__init__(None, height)
        self.calculate_jacket = self.calc_jacket()

    def __str__(self):
        return f'Ткани для костюма - {round(self.calculate_jacket, 2)} м2'


print("Расчет ткани для пальто")
print("Какой размер?")
c = int(input())
coat = Coat(c)
print(coat)
print("Расчет ткани для костюма")
print("Какой размер?")
j = int(input())
jacket = Jacket(j)
print(jacket)
cloth = Clothes(c, j)
print(cloth.calculate)


