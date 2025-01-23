import unittest
import countEvenNumbers

class TestCountEvenNumbers(unittest.TestCase):
	def test_that_count_even_numbers_exists(self):
		numbers = [1,5,7,3,2,9,8,10]
		actual = countEvenNumbers.countEvenNumbers(numbers)
		expected = 3
		self.assertEqual(actual, expected)


if __name__ ==("__main__"):
	unittest.main()