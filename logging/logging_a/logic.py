# Урок от Python Russian

import os

# Функция eval() работает следующим образом:
# - Анализирует выражение
# - Компилирует его в байт-код
# - Оценивает его как выражение Python
# - Возвращает результат оценки

# Пример:
# x = 1
# eval('x + 1') # 2
# eval('x++') # SyntaxError: invalid syntax

# Обычно eval() используется:
# - для оценки математических выражений
# - для преобразования строки в код

def calculate(exp: str):
    print(f"Get expression {exp}")
    try:
        result = eval(exp)
        print(f"Evaluated {result}")
        return result
    except Exception as e:
        print(f"Exception {e}")
        return None

if __name__ == "__main__":
    print(os.path.basename(__file__))