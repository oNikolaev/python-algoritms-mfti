from unittest import TestCase, main
from lection_06.sort_n2 import insertion_sort
from lection_06.sort_n2 import selection_sort
from lection_06.sort_n2 import bubble_sort


class SortingTest(TestCase):
    sort_algorithm = ""

    def test_insertion_sort(self):
        self.sort_algorithm = insertion_sort
        self.run_test_sort()

    def test_selection_sort(self):
        self.sort_algorithm = selection_sort
        self.run_test_sort()

    def test_bubble_sort(self):
        self.sort_algorithm = bubble_sort
        self.run_test_sort()

    def run_test_sort(self):
        self.run_test_sort_simple_list()
        self.run_test_range()
        self.run_test_duplicate_items()

    def run_test_sort_simple_list(self):
        A = [5, 2, 4, 1, 3]
        A_sorted = [1, 2, 3, 4, 5]
        self.sort_algorithm(A)
        self.assertTrue(A == A_sorted)

    def run_test_range(self):
        A = list(range(10, 20)) + list(range(0, 10))
        A_sorted = list(range(20))
        self.sort_algorithm(A)
        self.assertTrue(A == A_sorted)

    def run_test_duplicate_items(self):
        A = [4, 2, 4, 2, 1]
        A_sorted = [1, 2, 2, 4, 4]
        self.sort_algorithm(A)
        self.assertTrue(A == A_sorted)
