
from time import sleep
import threading


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            else:
                sleep(10)
                print(TrafficLight.__color[1])
                sleep(2)
            i += 1


print('Нажмите <Enter> для выхода')


def loop():
    while True:
        t = TrafficLight()
        t.running()


trheading.Thread(target=loop, daemon=True).start()
input()