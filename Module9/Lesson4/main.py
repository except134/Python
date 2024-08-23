import io
from random import choice

print("Lambda-функция")
print("==============")
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda c1, c2: c1==c2, first, second)))
print()

print("Замыкание")
print("=========")
def get_advanced_writer(file_name):
    file = open(file_name, "w", encoding='utf-8')

    def write_everything(*data_set):
        for i in data_set:
            file.writelines(str(i) + "\n")
        file.close()
    
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
print("Done\n")

print("Метод __call__")
print("==============")
class MysticBall():
    words = []
    
    def __init__(self, *words):
        self.words = words
    
    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Не знаю', 'Знаю', 'Не хочу')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print()
