import unittest

import MyArray

class MyTestCase(unittest.TestCase):

    fg .my_array = MyArray.MyArray(0)

    def test_that_my_array_is_empty(self):
        self.assertTrue(MyArray.is_empty(self))

    def test_that_my_array_is_not_empty(self):
        self.assertFalse(MyArray.empty())

    def test_that_my_array_contains_values(self):
        self.assertTrue(MyArray.add())

if __name__ == '__main__':
    unittest.main()
