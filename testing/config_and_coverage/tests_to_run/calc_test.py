from unittest import TestCase, main

from config_and_coverage.funcs_for_testing.calc import calculator


class CalculatorTest(TestCase):

    # Позитивные тесты
    def test_plus(self):
        self.assertEqual(calculator("2+2"), 4)

    def test_minus(self):
        self.assertEqual(calculator("2-5"), -3)

    def test_div(self):
        self.assertEqual(calculator("10/2"), 5.0)

    def test_mul(self):
        self.assertEqual(calculator("2*3"), 6)

    # Негативные тесты
    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("abrakadabra")
        self.assertEqual("Выражение должно содержать хотя бы один знак (+-/*)", e.exception.args[0])

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

