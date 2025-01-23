import unittest
from divide_or_square import divide_or_square

class TestDivideOrSquare(unittest.TestCase):
	def test_that_function_to_get_square(self):
		number = 40
		result = divide_or_square(number)
		expected = '6.32'
		self.assertEqual(result, expected)

	def test_that_divide_or_square_raise_exception_with_negative_input(self):
		self.assertRaises(ValueError, divide_or_square, -100)
			

	def test_that_divide_or_square_raise_exception_with_string_input(self):
		self.assertRaises(TypeError, divide_or_square, "fareedat")

	def test_that_divide_or_square_raise_exception_with_correct_input(self):
		number = 100
		result = divide_or_square(number)
		expected = '10.00'
		self.assertEqual(result, expected)
	
	def test_that_divide_or_square_raise_exception_with_none_input(self):
		self.assertRaises(TypeError, divide_or_square, " ")

	def test_that_divide_or_square_eaise_exception_with_rubbish(self):
		self.assertRaises(TypeError, divide_or_square, "hdhjh")