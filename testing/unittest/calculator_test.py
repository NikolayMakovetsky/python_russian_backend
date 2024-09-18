# Урок от Python Russian
from unittest import TestCase, main
from calculator import calculator
# https://docs.python.org/3/library/unittest.html#module-unittest

class CalculatorTest(TestCase):

    # При проверках функции мы не затрагиваем сложных глубоких тем:
    # Классы эквивалентности
    # Граничные значения
    # ...
    # В большинстве случаев для программиста достаточно сделать базовые проверки

    # "Red-Green" refactoring
    # пишем так, чтобы каждый написанный тест при первом запуске падал
    # (таким образом мы сразу убедимся в том, что тест работает верно)

    # начинаем писать с "позитивных" тестов (где все хорошо)
    def test_plus(self):
        self.assertEqual(calculator("2+2"), 4)

    def test_minus(self):
        self.assertEqual(calculator("2-5"), -3)

    def test_div(self):
        self.assertEqual(calculator("10/2"), 5.0)

    def test_mul(self):
        self.assertEqual(calculator("2*3"), 6)

    # далее пишем "негативные" тесты используя менеджер контекста
    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("abrakadabra")
        self.assertEqual("Выражение должно содержать хотя бы один знак (+-/*)", e.exception.args[0])
        # self.assertEqual("test", e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("2+2+2")
        self.assertEqual("Выражение должно содержать 2 целых числа и 1 знак", e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("2+*3")
        self.assertEqual("Выражение должно содержать 2 целых числа и 1 знак", e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator("2.34+3.54")
        self.assertEqual("Выражение должно содержать 2 целых числа и 1 знак", e.exception.args[0])

    def test_two_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator("a+b")
        self.assertEqual("Выражение должно содержать 2 целых числа и 1 знак", e.exception.args[0])

    # Мощный инструмент PyCharm - Coverage (покрытие)
    # Позволяет выявить те места кода, куда не "зашел" наш тест

    # Также PyCharm позволяет составить Конфигурации - список тестов
    # и запускать его нажатием одной кнопки

    # После того, как тесты написаны можно рефакторить код самой функции

if __name__ == '__main__':
    main() # main модуля unittest!