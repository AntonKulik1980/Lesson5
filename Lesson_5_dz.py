# Создать декоратор, который будет запускать функцию в отдельном
# потоке. Декоратор должен принимать следующие аргументы:
# название потока, является ли поток демоном.


from symbol import decorator
from functools import wraps
import time
from threading import Thread


def decorartor(name='first', daemon=False):
    def actual_decorartor(func):
        @wraps(func)
        def wrapper(*args):
            result = Thread(target=io_bound, args=(1, 3), name=name, daemon=daemon)

            return result

        return wrapper

    return actual_decorartor


@decorartor('second', True)
def io_bound(id_, sec):
    print(f'{id_} Уснула')
    time.sleep(sec)
    print(f'{id_} Проснулась')


result = io_bound('third', 5)
print(result)

# Создать функцию, которая будет скачивать файл из интернета по
# ссылке, повесить на неё декоратор, который будет запускать целевую
# функцию каждый раз в отдельном потоке. Создать список из 10
# ссылок, по которым будет происходить скачивание. Каждый поток
# должен сигнализировать, о том, что, он начал работу и по какой
# ссылке он работает, так же должен сообщать когда скачивание
# закончится.


import urllib.request


def download(url, location):
    urllib.request.urlretrieve(url, location)
    
    
download('https://i1.rozetka.ua/goods/13195269/samsung_sm_a107fzkdsek_images_13195269948.jpg',"d://in/Extracted")
    
    
    
    
    
    
