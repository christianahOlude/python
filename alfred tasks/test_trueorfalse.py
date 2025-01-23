import unittest
import true_or_false

class TestTrueOrFalse(unittest.TestCase):
	def test_that_true_or_false_exist(self):
		numbers = [1,4,5,2,5,9]
		actual = true_or_false.true_or_false(numbers)
		expected = [False,True,False,True,False,False]
		self.assertEqual(actual, expected)