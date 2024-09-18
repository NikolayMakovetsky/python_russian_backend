# Урок от Python Russian

import os
from menu import start
from logging import getLogger, basicConfig, DEBUG, ERROR, FileHandler, StreamHandler

# Handler - обработчик, который работает с теми событиями, которые фиксирует логгер

logger = getLogger() # главный root логгер от которого будем наследовать остальные
# ФОРМАТ: время/имялоггера/важность/сообщение
FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
file_handler = FileHandler("data.log")
file_handler.setLevel(DEBUG)
console = StreamHandler()
console.setLevel(ERROR)

# basicConfig(level=ERROR, format=FORMAT) # ЗАДАЕМ НУЖНЫЙ УРОВЕНЬ ЛОГИРОВАНИЯ
basicConfig(level=DEBUG, format=FORMAT, handlers=[file_handler, console]) # все в файл пишем

if __name__ == "__main__":
    print(os.path.basename(__file__))
    logger.info("start service")
    start()
    logger.info("stop service")

