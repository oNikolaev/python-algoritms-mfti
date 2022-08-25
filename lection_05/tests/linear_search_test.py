from unittest import TestCase, main
from lection_05.linear_search import array_search


class LinearSearchTest(TestCase):

    def test_find_item(self):
        A = [1, 2, 3, 4, 5]
        actual = array_search(A, 5, 2)
        expected = 1
        self.assertEqual(expected, actual)

    def test_not_find_item(self):
        A = [-1, -2, -3, -4, -5]
        actual = array_search(A, 5, -30)
        expected = -1
        self.assertEqual(expected, actual)

    def test_more_then_one(self):
        A = [10, 10, 20, 30, 40]
        actual = array_search(A, 5, 10)
        expected = 0
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
