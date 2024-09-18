import os
import threading
import time
from threading import Thread
from tkinter import *
from tkinter import ttk
from queue import Queue

    
# counter = [0]

# def inc():
#     c = counter[0]
#     time.sleep(0.1)
#     counter[0] = c + 1

queue = Queue()
queue.put(0)

def inc_queue():
    c = queue.get()
    time.sleep(0.1)
    queue.put(c+1)


if __name__ == "__main__":

    threads = [Thread(target=inc_queue, daemon=True) for _ in range(10)] 
    
    for t in threads:
        t.start()
    for t in threads:
        t.join() 
    print(queue.qsize())
    print(queue.get_nowait())
    # Нет Lock - нет возможностей для потенциального зависания программы!
    # Очереди потокобезопасны!
    # Свои очереди есть для asyncio, multithreading, multiprocessing


