from unittest import TestCase, main
from lection_05.cyclic_shift import shift_array


class CyclicShiftTest(TestCase):
    def test_left_shift(self):
        actual = [0, 1, 2, 3, 4]
        N = 5
        shift_array(actual, N, 'l')
        expected = [1, 2, 3, 4, 0]
        self.assertEqual(actual, expected)

    def test_right_shift(self):
        actual = [0, 1, 2, 3, 4]
        N = 5
        shift_array(actual, N, 'r')
        expected = [4, 0, 1, 2, 3]
        self.assertEqual(actual, expected)
