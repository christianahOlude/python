import unittest
import sum_of_number
import sum_numbers
import odd_numbers

class TestSumOfNumber(unittest.TestCase):
	def test_that_function_to_get_even(self):
		number = 1, 2, 3, 4, 5, 6
		actual = 2, 4
		expected = 2, 4
		self.assertEqual(actual, expected)
		
	def test_that_function_to_get_sum_of_number(self):
		number = 2, 4
		actual = sum_of_number.sum_of_number(number)
		expected = 6
		self.assertEqual(actual, expected)

	def test_that_function_to_sum_number(self):
		number = 54321
		actual = sum_numbers.sum_numbers(number)
		expected = 15
		self.assertEqual(actual, expected)

	def test_that_function_get_odd(self):
		number = 12345
		actual = odd_numbers.odd_numbers(number)
		expected = 9
		self.assertEqual(actual, expected)

	def test_that_function_multiply_numbers(self):
		number = 1234
		actual = multiply_numbers.multiply_numbers(number)
		expected = 30
		self.assertEqual(actual, expected)
		



if __name__ == "__main__":
	unittest.main()
		