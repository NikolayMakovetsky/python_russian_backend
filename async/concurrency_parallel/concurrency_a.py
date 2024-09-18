import time
import threading


def activity():
    for e in range(1000_000):
        abs(round(e ** 2 / 122) + e * 3.14)


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
    run(threaded=False) # Однопоточное исполнение 8.5 сек
    # run(threaded=True) # Десятипоточное исполнение 7.7 сек
    # Время исполнения почти не поменялось именно из-за работы GIL !!!
    # При исполнении CPU-bound задач GIL мешает,
    # Поскольку власть GIL распространяется на весь интерпретатор питона!
