import asyncio
import aiohttp
import requests
import time


async def one():
    print("Start one")
    await asyncio.sleep(1) # встань на паузу пока не выполнится asyncio.sleep(1)
    print("Stop one")


async def two():
    print("Start two")
    await asyncio.sleep(2) # закоментить и раскоментить строчку ниже
    # time.sleep(5) # для понимания работы event loop
    # По сути это ошибка использования внутри корутин
    # синхронного(блокирующего) кода, в том числе IO
    # Блокирующий код - код без await
    print("Stop two")


async def three():
    print("Start three")
    await asyncio.sleep(3)  # пока событие asyncio.sleep(3) не выполнится
                            # event loop эту корутину не тронет
    print("Stop three")     # после завершения кода корутины
                            # она автоматически удаляется из event loop


async def main(): # в асинхронке принято создавать корутину main
    # # Вариант 1: добавляй задачи по одной и в конце встань на паузу
    # asyncio.create_task(one()) # добавь в event loop функцию one()
    # asyncio.create_task(two())
    # await asyncio.create_task(three()) # встань на паузу пока не выполнится asyncio.create_task(three())

    # Вариант 2: gather(собери) все задачи в "пул" и выполни их
    await asyncio.gather(one(), two(), three())

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main()) # здесь под капотом создается и поддерживается event loop
    # пока все корутины из asyncio.run(main()) не выполнятся мы дальше не пойдем!
    print(time.time() - start)