import time
import threading
import requests


def activity():
    # for e in range(1000_000):
    #     abs(round(e ** 2 / 122) + e * 3.14)
    requests.get("https://ya.ru")


def run(threaded=False):
    start = time.time()
    if not threaded:
        for e in range(10):
            activity()
    else:
        threads = [threading.Thread(target=activity, daemon=True) for _ in range(10)]
        for e in threads:
            e.start()
        for e in threads:
            e.join()
    
    end = time.time()
    print(f"Time: {end - start} seconds")


if __name__ == "__main__":
    # run(threaded=False) # Однопоточное исполнение 1.4 сек
    run(threaded=True) # Десятипоточное исполнение 0.1 сек

    # В данном случае скорость исполнения существенно изменилась
    # Почему? Так как при исполнении IO-bound задач GIL не мешает
    # Поэтому при обращении к сайту, к файлу, к БД многопоточность эффективна!
