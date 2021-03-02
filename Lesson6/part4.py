from random import randrange
from time import sleep
import threading


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return f'{self.name} движется'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула на {direction}'

    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed}'


class TownCar(Car):
    max_s = 60

    def show_speed(self):
        if self.speed > self.max_s:
            return f'{self.name} превысила скорость! Скорость {self.speed}'
        else:
            return f'{self.name} едет со скоростью {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    max_s = 40

    def show_speed(self):
        if self.speed > self.max_s:
            return f'{self.name} превысила скорость! Скорость {self.speed}'
        else:
            return f'{self.name} едет со скоростью {self.speed}'


class PoliceCar(Car):
    pass


def randomize_turn(turn):
    rand_dict = randrange(3)
    my_dict = {0: "Лево", 1: "Право"}
    if rand_dict != 2:
        return turn(my_dict[rand_dict])
    else:
        return f'направление не изменилось'


print("Нажмите <Enter> для выхода")


def loop():
    while True:
        town = TownCar(randrange(1, 99), 'Красная', 'Киа', False)
        sport = SportCar(randrange(1, 120), 'Синяя', 'Порше', False)
        work = WorkCar(randrange(1, 80), 'Серый', 'Маз', False)
        police = PoliceCar(randrange(1, 120), 'Гос', 'Полиция', True)
        i = randrange(1, 8)
        sleep(2)
        if i != 3:
            print(town.go(), town.show_speed(), randomize_turn(town.turn))
        else:
            print(town.stop())
        sleep(2)
        if i != 5:
            print(sport.go(), sport.show_speed(), randomize_turn(sport.turn))
        else:
            print(sport.stop())
        sleep(2)
        if i != 8:
            print(work.go(), work.show_speed(), randomize_turn(work.turn))
        else:
            print(work.stop())
        sleep(2)
        if i != 6:
            print(police.go(), police.show_speed(), randomize_turn(police.turn))
        else:
            print(police.stop())
        sleep(2)

threading.Thread(target=loop, daemon=True).start()
input()
