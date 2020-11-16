# Создать декоратор, который будет запускать функцию в отдельном
# потоке. Декоратор должен принимать следующие аргументы:
# название потока, является ли поток демоном.


from symbol import decorator
from functools import wraps
import time
from threading import Thread
import random
import urllib.request
from abc import ABC, abstractmethod


def decorartor(name='first', daemon=False):
    def actual_decorartor(func):
        @wraps(func)
        def wrapper(*args):
            result = Thread(target=func, args=args, name=name, daemon=daemon)
            result.start()

        return wrapper

    return actual_decorartor


@decorartor('second', False)
def io_bound(id_, sec):
    print(f'{id_} Уснула')
    time.sleep(sec)
    print(f'{id_} Проснулась')


result = io_bound('10', 5)
print(result)


# Создать функцию, которая будет скачивать файл из интернета по
# ссылке, повесить на неё декоратор, который будет запускать целевую
# функцию каждый раз в отдельном потоке. Создать список из 10
# ссылок, по которым будет происходить скачивание. Каждый поток
# должен сигнализировать, о том, что, он начал работу и по какой
# ссылке он работает, так же должен сообщать когда скачивание
# закончится.


def run_async(func):
    from threading import Thread
    from functools import wraps

    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = Thread(target=func, args=args, kwargs=kwargs)

        print(f'{Thread.name} working')
        func_hl.start()
        print(f'{Thread.name} finished')
        return func_hl

    return async_func


if __name__ == '__main__':
    from time import sleep
    import urllib.request
    import random


    @run_async
    def download(i):

        filename = random.sample(range(1, 100), 1)
        location = f'C:\\Users\\1\\PycharmProjects\\itea_october\\Lesson5\\{filename}.png'
        urllib.request.urlretrieve(i, location)


    def main():
        list = ['https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.292.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.297.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.266.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.265.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.154.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.292.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.155.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.258.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.123.100.png',
                'https://evroplast.ru/cron_responsive/catalog/data/images/100/1.50.295.100.png']

        for i in list:
            download(i)


    main()


# Написать свой контекстный менеджер для работы с файлами.


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hello, world!')
