import unittest
import switch

class TestSwitchNumbers(unittest.TestCase):
	def test_that_switch_numbers_exist(self):
		numbers = (1,2,3,4,5)
		actual = switch.switch_numbers(numbers)
		expected = (3,4,5,1,2)
		                                                                                                                                                                                                                                                                                                                                                                                                                              self.assertEqual(actual, expected)

