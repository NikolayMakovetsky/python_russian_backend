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
    # ВАЖНО: НЕТ СМЫСЛА СОЗДАВАТЬ БОЛЬШЕ ПРОЦЕССОВ, ЧЕМ У НАС ЕСТЬ ЯДЕР
    else:
        processes = [Process(target=activity, daemon=True) for _ in range(10)]
        # processes = [Process(target=lambda: activity(), daemon=True) for _ in range(10)]
        # AttributeError: Can't pickle local object 'run.<locals>.<listcomp>.<lambda>'
        # Иными словами лямба функцию невозможно сериализовать при помощи pickle,
        # а это необходимое условие для передачи информации параллельно созданному
        # интерпретатору питона
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


def work(): # для 2 ядер
    """Список делим на кусочки, и каждый кусочек передаем отдельному процессу
    для подсчета суммы"""
    arr = list(range(1000_000))
    step = len(arr) // 2
    position = 0
    processes = [] # простой список для наших процессов
    for _ in range(2):
        split = arr[position: position + step] # срез исходного списка
        processes.append(Process(target=calc_sum_print, args=(split,), daemon=True))
        position += step
    start = time.time()
    for e in processes:
        e.start()
    for e in processes:
        e.join()
    end = time.time()
    print(f"Time: {end - start} seconds")


def work_pool(): # для 2 ядер
    arr = list(range(1000_000))
    step = len(arr) // 2
    start = time.time()
    with Pool(2) as pool:
        result = pool.map(calc_sum, [arr[position: position + step] for position in range(0, len(arr), step)])
        print(result)
    end = time.time()
    print(f"Time: {end - start} seconds")


if __name__ == "__main__":
    # work() # Time: 1.20 seconds
    work_pool() # Time: 0.83 seconds
    # Используй Pool, т.к. он ускоряет работу программы и делает код читабельнее



