from operator import contains
from time import sleep
import time 

class User:
    def __init__(self, name, password, age):
        self.name = name
        self.password = hash(password)
        self.age = age

    def checkpassword(self, password):
        if self.password == hash(password):
            return True
        else:
            return False

    def contain(self, string):
        index = self.name.find(string)
        if index != -1:
            return self.name

    def __str__(self):
        return self.name

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
        
    def contain(self, string):
        selftitle = self.title.lower()
        index = selftitle.find(string.lower())
        if index != -1:
            return selftitle

    def play_video(self):
        for i in range(self.duration):
            print(i + 1, end=" ")
            time.sleep(1)
        print("Конец видео")    

class UrTube:
    def __init__(self):
        self.videos = []
        self.users = []
        self.current_user = str()

    def add(self, *videos):
        for i in videos:
            self.videos.append(i)

    def get_videos(self, title):
        ret = []
        for i in self.videos:
            if i.contain(title):
                ret.append(i.title)
        return ret

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео!")    
        else:
            for i in self.videos:
                if i.contain(title):
                    if i.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу!")
                        return
                    else:
                        i.play_video()
                        return
            print("Такого видео не существует!")  
        
    def log_out(self):
        for i in self.users:
            if i.contain(name):
                del i
                return

    def register(self, name, password, age):
        for i in self.users:
            if i.contain(name):
                print(f"Пользователь {name} уже существует!")  
                return
                
        self.users.append(User(name, password, age))
        self.current_user = self.users[len(self.users) - 1]
    
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
