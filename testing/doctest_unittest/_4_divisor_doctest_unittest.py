from unittest import TestCase, main
import doctest

import _2_divisor_doctest
from _2_divisor_doctest import divide


def load_tests(loader, tests, ignore):
    """
    Функция из документации unittest
    Unittest, когда будет искать все свои тестовые файлы, оканчивающиеся на '*test.py'
    (а мы настроили, чтобы он искал их в папке данного проекта)
    добавит к ним и прогонит все найденные DOCTESTS! из модуля _2_divisor_doctest"""
    tests.addTests(doctest.DocTestSuite(_2_divisor_doctest))
    return tests


class TestDivisor(TestCase):
    def test_zero_raises(self):
        with self.assertRaises(ValueError) as e:
            divide(10, 0)
        self.assertEqual("На ноль делить нельзя", e.exception.args[0])


if __name__ == '__main__':
    main()