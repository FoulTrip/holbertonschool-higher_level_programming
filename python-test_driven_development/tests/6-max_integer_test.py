#!/usr/bin/python3

import unittest

"""
    Max integer - Unittest
"""


class TestMaxInteger(unittest.TestCase):
    """Unittests for the function max_integer()"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_values(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_negative_values(self):
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)

    def test_mixed_values(self):
        self.assertEqual(max_integer([-1, 3, 0, -4]), 3)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)


def max_integer(list=[]):
    if not list:
        return None
    max_value = list[0]
    for num in list:
        if num > max_value:
            max_value = num
    return max_value
