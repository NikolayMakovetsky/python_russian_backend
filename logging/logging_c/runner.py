# Урок от Python Russian
import json
import os
import logging.config
from logging import getLogger
from menu import start

with open("logging.conf") as file:
    config = json.load(file)

logging.config.dictConfig(config)
logger = getLogger()



if __name__ == "__main__":
    print(os.path.basename(__file__))
    logger.info("start service")
    start()
    logger.info("stop service")

