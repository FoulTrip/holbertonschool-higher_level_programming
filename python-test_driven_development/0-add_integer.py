#!/usr/bin/python3

"""
 Integers addition
"""


def add_integer(a, b=98):
    """
    Returns the addition of two integers.
    """

    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
