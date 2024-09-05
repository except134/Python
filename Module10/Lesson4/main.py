from queue import Queue
from random import randrange
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def Run(self):
        sleep(randrange(3, 10))

class Cafe:
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = list(args)

    def guest_arrival(self, *guests):
        for g in guests:
            for t in self.tables:
                if t.guest is None:
                    t.guest = g
                    g.start()
                    print(f"{g.name} сел(-а) за стол номер {t.number}")
                    break
            else:
                self.queue.put(g)
                print(f"{g.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(t.guest is not None for t in self.tables):
            for t in self.tables:
                if t.guest is not None and not t.guest.is_alive():
                    print(f'{t.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {t.number} свободен')
                    t.guest = None
                
                if not self.queue.empty():
                    ng = self.queue.get()
                    t.guest = ng
                    ng.start()
                    print(f"{ng.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}")

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

