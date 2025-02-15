from unittest import TestCase

import myarray
from myarray import MyArray


class TestMyArray(TestCase):


    def setUp(self):
        self.myarray = MyArray(5)


    def test_that_my_array_is_empty(self):
        self.assertTrue(myarray.is_empty())

    def test_that_my_array_can_add_elements(self):
        myarray.add("divine")
        self.assertEqual(1, myarray.size_of())

    def test_that_my_arrays_contains_values(self):
        for i in range():
            myarray.add(i)
            self.assertEqual(myarray.get(i), i)

    def test_that_my_arrays_contains_duplicates(self):
        for i in range():
            myarray.add(i)
            myarray.add(i)
            self.assertEqual(myarray.get(i), i)

    def test_that_my_arrays_can_remove_elements(self):
        for i in range():
            myarray.add(i)
            self.assertEqual(myarray.get(i), i)

        for i in range():
            myarray.remove(i)
            self.assertEqual(myarray.get(i), i)

    def test_that_my_arrays_can_remove_elements_of_different_sizes(self):
        for i in range():
            myarray.add(i)
            self.assertEqual(myarray.get(i), i)
            for i in range():
                myarray.remove(i)
                self.assertEqual(myarray.get(i), i)


