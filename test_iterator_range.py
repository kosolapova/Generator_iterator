import unittest

from iterator_range import IterRange

class IterRangeTests(unittest.TestCase):

    def test_iterator_direct(self):
        self.assertEqual([i for i in IterRange(10)], [i for i in range(10)])
        self.assertEqual([i for i in IterRange(10, 2, 2)], [i for i in range(2, 10, 2)])
        self.assertEqual([i for i in IterRange(100, 2, 3)], [i for i in range(2, 100, 3)])

    def test_generator_backward(self):
        self.assertEqual([i for i in IterRange(0,9,-1)], [i for i in range(9,0,-1)])
        self.assertEqual([i for i in IterRange(0,100,-10)], [i for i in range(100,0,-10)])


    def test_iterator_empty(self):
        self.assertEqual([i for i in IterRange(0, 0, -1)], [i for i in range(0, 0, -1)])
        self.assertEqual([i for i in IterRange(10, 0, -5)], [i for i in range(0, 10, -5)])

    def test_iterator_zero(self):
        self.assertEqual([i for i in IterRange(0, 1, 1)], [i for i in range(1, 0, 1)])
