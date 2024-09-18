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
    

if __name__ == "__main__":
    # Важно понять, что порой нам нужна многопоточность не для того, чтобы выиграть время
    # а для того, чтобы главный процесс продолжил свою работу!!!
    tk = Tk()
    button1 = ttk.Button(tk, text = "WAIT", command = lambda: waiting(3))
    button1.pack(side=LEFT)
    # При нажатии на кнопку "WAIT" весь интерфейс на время замирает, что очень плохо

    button2 = ttk.Button(tk, text = "THREAD", command = lambda: thread_wait(3))
    button2.pack(side=LEFT)
    tk.mainloop()

