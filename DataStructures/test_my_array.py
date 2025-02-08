import unittest
from MyArray import MyArray

class MyTestCase(unittest.TestCase):


    def test_that_my_array_is_empty(self):
        my_array = MyArray(0)
        self.assertTrue(my_array.is_empty())

    def test_that_my_array_can_add_elements(self, size):
        my_array = MyArray(1)
        my_array.add("divine")
        self.assertEqual(1, size())

    def test_that_my_arrays_contains_values(self, size):
        my_array = MyArray(size)
        for i in range(size):
            my_array.add(i)
            self.assertEqual(my_array.get(i), i)

    def test_that_my_arrays_contains_duplicates(self, size):
        my_array = MyArray(size)
        for i in range(size):
            my_array.add(i)
            my_array.add(i)
            self.assertEqual(my_array.get(i), i)

    def test_that_my_arrays_can_remove_elements(self, size):
        my_array = MyArray(size)
        for i in range(size):
            my_array.add(i)
            self.assertEqual(my_array.get(i), i)

        for i in range(size):
            my_array.remove(i)
            self.assertEqual(my_array.get(i), i)

    def test_that_my_arrays_can_remove_elements_of_different_sizes(self, size):
        my_array = MyArray(size)
        for i in range(size):
            my_array.add(i)
            self.assertEqual(my_array.get(i), i)
            for i in range(size):
                my_array.remove(i)
                self.assertEqual(my_array.get(i), i)

    def test_that_my_arrays_can_be_sorted(self, size):
        my_array = MyArray(size)
        for i in range(size):
            my_array.add(i)
            my_array.add(i)
            self.assertEqual(my_array.get(i),



if __name__ == '__main__':
    unittest.main()
