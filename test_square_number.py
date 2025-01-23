import unittest
import square_number
import name_bool
import alphanum
import get_double
#import greater_than_five
import get_sum
import even
import my_dict_in_zip

class TestSquareNumbers(unittest.TestCase):
	def test_that_square_number_exists(self):
		number = [4]
		actual = square_number.square_number()
		expected = [1, 4, 9 ,16]
		self.assertEqual(actual, expected)

	def test_that_name_bool_exists(self):
		name = ['madam', 'ápple', 'racecar']
		actual = name_bool.name_bool(name)
		expected = [True, False, True]
		self.assertEqual(actual, expected)

	def test_that_alphanum_exists(self):
		name = 'abc123def456'
		actual = alphanum.alphanum(name)
		expected = [1,2,3,4,5,6]
		self.assertEqual(actual, expected)

	def test_that_get_double_exists(self):
		number = [1,2,3]
		actual = get_double.get_double()
		expected = [2,4,6]
		self.assertEqual(actual, expected)

	#def test_that_get_five_exists(self):
		#names= ["Apple","Fish","Orange","Ice","Lime"]
		#actual = greater_than_five.greater_than_five(names)
		#expected = ["Apple","Orange"]
		#self.assertEqual(actual, expected)

	def test_that_get_sum_exists(self):
		number = 1,9,2,3,7,4
		actual =get_sum.get_sum(number)
		expected = 26
		self.assertEqual(actual, expected)

	def test_that_even_exists(self):
		number = 10
		actual = even.even(number)
		expected = {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
		self.assertEqual = (actual, expected)

	def test_that_keys_and_values_exists(self):
		keys = ["name","age","city"]
		values = ["Alice",25,"NewYork"]

	def test_that_my_dict_in_zip_exists(self):
		actual = my_dict_in_zip.my_dict_in_zip('keys', 'values')
		expected = {name: Alice, age: 25, city: NewYork}
		self.assertEqual(actual, expected)

if __name__ ==("__main__"):
	unittest.main()