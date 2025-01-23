import unittest

from function.Encrypt import encrypt


class TestEncrypt(unittest.TestCase):
    def test_that_encrypt_text_function_exists(self):
        self.assertTrue(encrypt("Hello World!", 13))  # add assertion here

    def test_that_functon_returns_true_value(self):
        self.assertTrue(encrypt("Uryyb, Jbeyq!", 13))



if __name__ == '__main__':
    unittest.main()
