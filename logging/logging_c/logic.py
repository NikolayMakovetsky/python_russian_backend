# Урок от Python Russian

import os
from logging import getLogger

logger = getLogger(__name__) # создай логгер с именем данного модуля



def calculate(exp: str):
    logger.debug("Get expression %s", exp)
    try:
        result = eval(exp)
        logger.debug("Evaluated %s", result)
        return result
    except Exception as e:
        logger.error("Exception %s", e)
        return None

if __name__ == "__main__":
    print(os.path.basename(__file__))