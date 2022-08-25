from unittest import TestCase, main
from lection_05.invert_array_demo import invert_array


class InvertArrayTest(TestCase):

    def test_invert_array(self):
        actual = [1, 2, 3, 4, 5]
        N = 5
        expected = [5, 4, 3, 2, 1]
        invert_array(actual, N)
        self.assertEqual(expected, actual)

    def test_invert_duplicate_array(self):
        actual = [0, 0, 0, 0, 0, 0, 0, 10]
        N = 8
        expected = [10, 0, 0, 0, 0, 0, 0, 0]
        invert_array(actual, N)
        self.assertEqual(expected, actual)
