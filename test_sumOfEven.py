import unittest
import sum_of_even

class TestSumOfEven(unnittest.TestCase):
	def test_that_sum_of_even_exists(self):
		numbers = (2,7,9,17,19,2,8,10)
		actual = sum_of_even.sum_of_even(numbers)
		expected = 2,2,8,10
		self.assertEqual(actual, expected)


if __name__ ==("__main__"):
	unittest.main()