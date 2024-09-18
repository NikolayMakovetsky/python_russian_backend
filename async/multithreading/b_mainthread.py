import os
import threading
import time
from threading import Thread
from tkinter import *
from tkinter import ttk


def waiting(timeout):
    """Ожидание указанного кол-ва секунд (имитация некой работы)"""
    while timeout > 0:
        timeout -= 1
        time.sleep(1)
    print("OK")


def thread_wait(timeout):
    """Вызов функции waiting в потоке"""
    thread = Thread(target=waiting, args=(timeout,), daemon=True)
    thread.start()
    return thread
    
counter = [0]
def inc():
    c = counter[0]
    time.sleep(0.1)
    counter[0] = c + 1

def info():
    """Вывод id процесса и name текущего потока"""
    # Процесс = программа
    # Один содержит как минимум один поток
    pid = os.getpid() # Получение у ОС id процесса
    name = threading.current_thread().name # Получение имени текущего потока
    print(f"Process {pid}, name {name}")


if __name__ == "__main__":
    info() # Process 11024, name MainThread