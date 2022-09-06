from unittest import TestCase, main
from lection_06.counting_sort import counting_sort


class CountingSort(TestCase):
    def test_counting_sort(self):
        A = [8, 6, 7, 9, 3, 4, 7, 6, 1, 1]
        A_sorted = [1, 1, 3, 4, 6, 6, 7, 7, 8]
        A_result = counting_sort(A)
        self.assertTrue(A_result == A_sorted)
        pass
