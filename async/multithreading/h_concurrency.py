import time
from concurrent.futures import ThreadPoolExecutor
import requests


def activity():
    requests.get("https://yandex.ru")
    print("OK")


def run(threaded=False):
    start = time.time()
    if not threaded:
        for e in range(10):
            activity()
    else:
        executor = ThreadPoolExecutor() # создаем исполнителя executor
                                        # вся многопоточность спрятана под капотом!
        for _ in range(10):
            executor.submit(activity)   # передаем исполнителю задачу (10 шт в цикле)
        executor.shutdown(wait=True)    # завершится, но дождаться всех потоков
    end = time.time()
    print(f"Time: {end - start} seconds")


if __name__ == "__main__":
    run(threaded=True)

    # ThreadPoolExecutor() экономит ресурсы
    # При старте он сам создает нужное кол-во потоков (обычно равное кол-ву ядер
    # системы, но можно указать и свое кол-во) и он их не убивает, они все время висят,
    # а тем самым он экономит ресурсы, т.к. не обращается каждый раз к системе, чтобы
    # то создать, то убить поток...
    # Вы кидаете ему задачи, он находит какой поток более-менее свободный и передает
    # задачу именно этому потоку...
    # при этом программисту не нужно писать start(), join() и прочее...
