import asyncio
import aiohttp # для работы с интернет-запросами
# import aiopg # Для работы с бд постгрес
# import aio... спец библиотеки специально для асинхронных запросов
#               к тому или иному ресурсу...
import requests
import time

# Блокирующие запросы также вредны асинхронке как и любые другие блокирующие задачи!

async def blocking():
    resp = requests.get("https://ya.ru") # пока get не вернет данные дальше выполнение не идет
    print(resp.status_code)


async def async_http():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://ya.ru') as resp: # асинхронный get
            print(resp.status)
# идеальная асинхронка - это когда внутри нее у нас только async или await
# print - тоже блокирующий, но он быстрый, потому тут мы не заморачиваемся


async def main():
    # await asyncio.gather(*(blocking() for _ in range(5))) # time = 0.65 sec.
    await asyncio.gather(*(async_http() for _ in range(5))) # time = 0.16 sec.


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)