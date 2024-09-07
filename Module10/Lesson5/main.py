from datetime import datetime
import multiprocessing
import os

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

def linear():
    start = datetime.now()
    for f in filenames:
        read_info(f)
    end = datetime.now()
    print(f'{end - start} (линейный)')

def multiprocessor():
    print(f'Используем {os.cpu_count()} потоков')
    with multiprocessing.Pool() as p:
        start = datetime.now()
        p.map(read_info, filenames)
        end = datetime.now()
    print(f'{end - start} (многопроцессный)')

if __name__ == '__main__':
    linear()
    multiprocessor()

