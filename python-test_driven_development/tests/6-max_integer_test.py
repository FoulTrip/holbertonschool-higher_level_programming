#!/usr/bin/python3

import unittest

"""
    Max integer - Unittest
"""

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for the function max_integer()"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_positive_values(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_negative_values(self):
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)
        self.assertEqual(max_integer([-5, -5, -5, -5, -5]), -5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_values(self):
        self.assertEqual(max_integer([-1, 3, 0, -4]), 3)
        self.assertEqual(max_integer([0, -1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, 0, 2, 1]), 2)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-2, -2, -2, -2, -2]), -2)

    def test_list_of_one_element(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-3]), -3)
        self.assertEqual(max_integer([0]), 0)


if __name__ == "__main__":
    unittest.main()
