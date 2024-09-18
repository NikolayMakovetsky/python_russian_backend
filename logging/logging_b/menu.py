# Урок от Python Russian
import os
from logic import calculate
from logging import getLogger

logger = getLogger(__name__) # создай логгер с именем данного модуля

def start():
    while True:
        expression = input("Введите выражение для вычисления: ")
        logger.debug("Expression is %s", expression) # log
        if not expression:
            logger.info("empty expression...stopping") # log
            break
        result = calculate(expression)
        if result is None:
            logger.info("No result back...stopping") # log
            break
        print(f"Result is {result}") # info for user


if __name__ == "__main__":
    print(os.path.basename(__file__))