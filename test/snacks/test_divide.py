import unittest
import divide
import squareroot

class TestDivideFunction(unittest.TestCase):
	def test_that_function_exists(self):
		divide.get_divide(5) 
		
	def test_that_divide_function_returns_correct_value(self):
		actual = divide.get_divide(25)
		expected = 5
		self.assertEqual(actual, expected)
		
		
	def test_that_squareroot_function_returns_correct_value(self):
		actual =  squareroot.get_squareroot(10)
		expected = 3.16
		self.assertEqual(actual, expected)

if __name__ ==("__main__"):
	unittest.main()