import unittest
import menstrual_app

class TestMenstrualApp(unittest.TestCase):
	def test_that_menstrual_app_exists(self):
		name = blessing
		actual = menstrual_app.mestrual_app(name)
		expected = blessing
		self.assertEqual(actual, expected)