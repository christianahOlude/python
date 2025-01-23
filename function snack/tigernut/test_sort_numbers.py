import unittest
import sort_numbers

class TestSortNumbers(unittest.TestCase):
	def test_that_sort_numbers_exists(self):
		numbers = [3,4,5,10]
		numbers1 = [1,7,8,9]
		actual = sort_numbers.sort_numbers(numbers,numbers1)
		expected = [1,3,4,5,7,8,9,10]
		self.assertEqual(actual,expected)


if __name__ == "__main__":
	unittest.main()





