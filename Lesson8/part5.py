class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print('Сумма равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print('Произведение равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'



z_1 = ComplexNumber(int(input('Введите 1е вещественое число 1го комплексного числа\n')), \
                    int(input('Введите 2е вещественое число 1го комплексного числа\n')))
z_2 = ComplexNumber(int(input('Введите 1е вещественое число 2го комплексного числа\n')), \
                    int(input('Введите 2е вещественое число 2го комплексного числа\n')))
print(z_1 + z_2)
print(z_1 * z_2)