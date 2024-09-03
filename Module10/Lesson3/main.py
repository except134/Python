import time
import random
from threading import Thread, Lock

class Bank:
    def __init__(self):
        self.balance = 500
        self.lock = Lock()
        super().__init__()

    def deposit(self):
        for i in range(100):
            bal = random.randint(50, 500)
            self.balance += bal

            if self.balance >= 500 and self.lock.locked(): 
                self.lock.release()

            print(f"Пополнение: {bal}. Баланс: {self.balance}")
            time.sleep(0.001)
        
    def take(self):
        for i in range(100):
            bal = random.randint(50, 500)
            print(f"Запрос на {bal}")

            if bal <= self.balance: 
                self.balance -= bal
                print(f"Снятие: {bal}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()

            time.sleep(0.001)
    
bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
