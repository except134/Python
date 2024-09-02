import time
from threading import Thread

class Knight(Thread):
    name = ""
    power = 0
    __enemies = 100

    def __init__(self, name, power):
        self.name = name
        self.power = power
        super().__init__()
    
    def run(self):
        print(f"{self.name} на нас напали!", flush=True)

        count = 0
        while(self.__enemies != 0):
            self.__enemies -= self.power
            count += 1
            time.sleep(1)
            print(f"{self.name} сражается {count}..., осталось {self.__enemies} воинов.", flush=True)

        print(f"{self.name} одержал победу спустя {count} дней(дня)!", flush=True)
            
# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
