import unittest
import cryptography

class TestFunctionEncrypt(unittest.TestCase):		
	def test_that_function_encrypt_exists(self):
		encrypt("app", 3)

	def test_that_encrypt_returns_correct_value(self):
		actual = encrypt("app",3)
		expected = "dss"
		self.assertEqual(actual, expected)

	def test_that_encrypt_returns_correct_with_spaces(self):
		actual = encrypt("a pp",3)
		expected = "d#ss"
		self.assertEqual(actual, expected)


class TestFunctionDecrypt(unittest.TestCase):
	def test_that_function_decrypt_exists(self):
		decrypt("dss",3)

	def test_that_function_decrypt_returns_correct_value(self):
		actual = decrypt("dss",3)
		expected = "app"
		self.assertEqual(actual, expected)

	def test_that_function_decrypt_returns_correct_value(self):
		actual = decrypt("d#ss", 3)
		expected = "a pp"
		self.assertEqual(actual, expected)
