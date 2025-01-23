import unittest
import true_or_false
import sum_of_even

class TestTrueOrFalse(unittest.TestCase):
	def test_that_true_or_false_exists(self):
		numbers = [10,3,7,1.9,4,2,8,5,6]
		actual = true_or_false.true_or_false(numbers)
		expected = [True,false,false,false,false,true,true,true.false,true]
		self.assertEqual(actual, expected)

	def test_that_sum_of_even_exists(self):
		numbers = 2,7,9,17,19,2,8,10
		actual = sum_of_even.sum_of_even(numbers)
		expected = 2,2,8,10
		self.assertEqual(actual, expected)
	def test_that_sum_of_even_exists(self):
		numbers = 2,2,8,10
		actual = sum_of_even.sum_of_even(numbers)
		expected = 22
		self.assertEqual(actual, expected)

	def test_that_multiple_of_three_exists(self)
		numbers = [3, 30]
		actual = multiple_of_three.multipe_of_three(numbers)
		expected = [3,6,9,12,15,18,21,24,27,30]
		self.assertEqual(actual, expected)



