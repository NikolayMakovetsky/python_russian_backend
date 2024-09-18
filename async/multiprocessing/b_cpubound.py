import time
from multiprocessing import Process, Pool
import requests
# СИНТАКСИС multiprocessing ОЧЕНЬ ПОХОЖ НА СИНТАКСИС multithreading

def activity():
    result = 0
    for e in range(1000_000):
        result += abs(round(e ** 2 / 122) + e * 3.14) # CPU-bound задача
    print(result)
    # requests.get("https://ya.ru") # IO-bound задача
    # print("OK")


def run(parallel=False):
    start = time.time()
    if not parallel:
        for e in range(10):
            activity()
    else:
        processes = [Process(target=activity, daemon=True) for _ in range(10)]
        for e in processes:
            e.start()
        for e in processes:
            e.join()
    
    end = time.time()
    print(f"Time: {end - start} seconds")


def calc_sum(a_list: list):
    return sum(a_list)


def calc_sum_print(a_list: list):
    print(sum(a_list))



if __name__ == "__main__":
    # run(parallel=False)   # Time: 8.61 seconds
    run(parallel=True)      # Time: 6.52 seconds

