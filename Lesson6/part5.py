
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки.'


class Pen(Stationery):

    def __init__(self):
        super().__init__('Ручкой')

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):

    def __init__(self):
        super().__init__('Карандашом')

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):

    def __init__(self):
        super().__init__('Маркером')

    def draw(self):
        return f'Запуск отрисовки {self.title}'


p = Pen()
n = Pencil()
h = Handle()
print(p.draw())
print(n.draw())
print(h.draw())
