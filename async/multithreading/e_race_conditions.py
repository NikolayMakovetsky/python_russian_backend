import os
import threading
import time
from threading import Thread
from tkinter import *
from tkinter import ttk

    
counter = [0]
def inc():
    c = counter[0]
    time.sleep(0.1) # имитация ГОНКИ ПОТОКОВ
    # GIL дает поработать каждому потоку 5 мс, а задержка 0.1 сек гораздо больше
    counter[0] = c + 1


if __name__ == "__main__":

    threads = [Thread(target=inc, daemon=True) for _ in range(100)] 
    
    for t in threads:
        t.start()
    for t in threads:
        t.join() 
    print(counter)
    # Результат ГОНКИ ПОТОКОВ:
    # Все 100 потоков зашли в функцию (гонка за ресурс), взяли значение 0
    # Далее благодаря time.sleep(0.1) GIL передавал приоритет работы след. потоку
    # В результате все потоки перезаписывали в переменную одно и тоже значение: 1
    # ВЫВОД: ОТ ГОНКИ ЗА РЕСУРС GIL НЕ ЗАЩИЩАЕТ !!!
