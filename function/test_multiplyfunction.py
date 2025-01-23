from unittest import TestCase
import multiply

class TestMultiplyFunction(TestCase):
	def test_that_function_exists(self):
		multiply.get_multiply(2, 3)

	def test_that_function_returns_correct_value(self):
		actual = multiply.get_multiply(2, 2)
		expected = 4
		self.assertEqual(actual, expected)

	def test_that_multiply_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, multiply.get_multiply, "going")
 
