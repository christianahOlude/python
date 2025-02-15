import unittest

from dsa.queue import Queue


class TestQueue(unittest.TestCase):
    def test_that_queue_is_empty(self):  # add assertion here
        queue = Queue(MyArray)
        self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    unittest.main()
