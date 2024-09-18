import os
import threading
import time
from threading import Thread
from tkinter import *
from tkinter import ttk

    
counter = [0]
lock = threading.Lock()

def inc():
    lock.acquire() # установить блокировку (только 1 поток может зайти внутрь)
    c = counter[0]
    time.sleep(0.1)
    counter[0] = c + 1
    lock.release() # отпустить блокировку
    # если забудем использовать release или по условию не зайдем в эту строчку кода,
    # то получим DEADLOCK "ЗАВИСАНИЕ"
    # Иногда поток блокирует сам себя, иногда блокирует других, много вариантов


if __name__ == "__main__":

    threads = [Thread(target=inc, daemon=True) for _ in range(10)] 
    
    for t in threads:
        t.start()
    for t in threads:
        t.join() 
    print(counter)
    # Чтобы предотвратить гонку за ресурс используй блокировки
