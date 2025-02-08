import unittest

import calculator
from calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_that_ten_positive_number_can_be_added(self):
        calc = Calculator()
        number = 30
        nun = 45
        result = calc.addition(number, nun)
        self.assertEqual(result, 75)

    def test_that_negative_number_can_be_added(self):
        calc = Calculator()
        number_one = 1
        number_two = 2
        result = calc.adbbby(number_one, number_two)
        self.assertEqual(result, 3)

    def test_that_string_raise_value_error(self):
        calc = Calculator()
        name = "ola"
        result = calc.raise_value_error(name)
        self.assertEqual(result, ValueError)

    def test_that_function_gets_float(self):
        calc = Calculator()
        number_one = 3.14
        number_two = 3.13
        result = calc.gets_float(number_one, number_two)
        self.assertEqual(result, 6.27)


if __name__ == '__main__':
    unittest.main()
