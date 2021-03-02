

class Road:
    __weight = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, data):
        return data * self.__weight * self._width * self._length / 1000


print("Введите длину дороги, м")
length = int(input())
print("Введите ширину дороги, м")
width = int(input())
road = Road(length, width)
print("Введите толщину покрытия, см")
print(road.weight(int(input())), "т")



