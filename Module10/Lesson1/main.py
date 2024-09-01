import io, time
from threading import Thread

def get_time_track(precision, text):
    def time_track(func):
        def surrogate(*args, **kwargs):
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            elapsed = round(ended_at - started_at, precision)  
            print(f"{text} {elapsed} секунд(ы)")
            return result
        return surrogate
    return time_track

#@get_time_track(precision=2, text="Функция работала")
def write_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i + 1}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")    

@get_time_track(precision=2, text="Работа потоков")
def NoThreads():
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")

@get_time_track(precision=2, text="Работа потоков")
def WithThreads():
    t1 = Thread(target=write_words, args=(10, "example5.txt"))
    t2 = Thread(target=write_words, args=(30, "example6.txt"))
    t3 = Thread(target=write_words, args=(200, "example7.txt"))
    t4 = Thread(target=write_words, args=(100, "example8.txt"))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()

NoThreads()
print()
WithThreads()
