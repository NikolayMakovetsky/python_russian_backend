# Урок от Python Russian
import os
from logic import calculate

def start():
    while True:
        expression = input("Введите выражение для вычисления: ")
        print(f"Expression is {expression}") # log
        if not expression:
            print(f"empty expression...stopping") # log
            break
        result = calculate(expression)
        if result is None:
            print(f"No result back...stopping") # log
            break
        print(f"Result is {result}") # info for user


if __name__ == "__main__":
    print(os.path.basename(__file__))