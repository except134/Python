from operator import contains
from time import sleep 

class User:
    pass

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
        
    def contain(self, string):
        return contains(self.title, string)

class UrTube:
    def __init__(self):
        self.videos = []

    def add(self, *videos):
        for i in videos:
            self.videos.append(i)

    def get_videos(self, title):
        ret = []
        for i in self.videos:
            if i.contain(title):
                ret.append(i.title)
        return ret
    
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
#ur.watch_video('Для чего девушкам парень программист?')
#ur.register('vasya_pupkin', 'lolkekcheburek', 13)
#ur.watch_video('Для чего девушкам парень программист?')
#ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
#ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
#ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
#print(ur.current_user)

# Попытка воспроизведения несуществующего видео
#ur.watch_video('Лучший язык программирования 2024 года!')
