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
    

def info():
    """Вывод id процесса и name текущего потока"""
    # Процесс = программа
    # Один процесс содержит как минимум один поток
    # На уровне ОС есть ограничение на кол-во потоков в одном процессе
    # Потоки - не сущности внутри питона, а настоящие потоки ОС! (диспетч.задач)
    pid = os.getpid() # Получение у ОС id процесса
    name = threading.current_thread().name # Получение имени текущего потока
    print(f"Process {pid}, name {name}")


if __name__ == "__main__":

    threads = [Thread(target=info, daemon=True) for _ in range(10)] # создаем 10 потоков
    # daemon=True говорит питону убить все второстепенные потоки в момент,
    # когда завершится главный MainThread поток 
    
    for t in threads:
        t.start() # стартуем 10 потоков
    for t in threads:
        t.join() # говорим программе: "дожидись выполнения 10 потоков" (а не убивай их)
    
    info()
    # Как видим id процесса везде одно и то же!