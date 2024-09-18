import os
import threading
import time
from threading import Thread
from tkinter import *
from tkinter import ttk


    
counter = [0]
def inc():
    c = counter[0]
    counter[0] = c + 1


if __name__ == "__main__":

    threads = [Thread(target=inc, daemon=True) for _ in range(10_000)] 
    
    for t in threads:
        t.start()
    for t in threads:
        t.join() 
    print(counter)
    # Ждем выполнения уже некоторое время
    # Важно: создание потока ОС - "дорогая" по времени операция! - ЭТО МИНУС!
    # ЕЩЕ ОДИН МИНУС - потенциальная ГОНКА ПОТОКОВ (race conditions)
    # В питоне GIL не дает произойти гонке потоков, а вот 
    # в Java нет GIL, поэтому потоки могут "перемешиваться"
    # и результат будет не 10000, а например 8743
    # GIL гарантирует, что в единицу времени работает ТОЛЬКО 1 ПОТОК
    # А вот в JAVA, C# нужна синхронизация потоков...
