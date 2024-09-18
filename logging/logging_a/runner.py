# Урок от Python Russian

import os
from menu import start


if __name__ == "__main__":
    print(os.path.basename(__file__))
    print("start service")
    start()
    print("stop service")

