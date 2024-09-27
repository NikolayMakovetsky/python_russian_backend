from unittest import TestCase, main
import doctest

from config_and_coverage.funcs_for_testing import div


def load_tests(loader, tests, ignore):
    """
    Функция подключающая Doctest к Unittest"""
    tests.addTests(doctest.DocTestSuite(div))
    return tests


class TestDivisor(TestCase):
    def test_zero_raises(self):
        with self.assertRaises(ValueError):
            div.divide(10, 0)
