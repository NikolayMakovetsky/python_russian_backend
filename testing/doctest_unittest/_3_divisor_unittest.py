from unittest import TestCase, main

from _2_divisor_doctest import divide


class TestDivisor(TestCase):
    def test_zero_raises(self):
        with self.assertRaises(ValueError) as e:
            divide(10, 0)
        self.assertEqual("На ноль делить нельзя", e.exception.args[0])


if __name__ == '__main__':
    main()