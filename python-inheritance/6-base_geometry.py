#!/usr/bin/python3

"""
This script defines a class 'BaseGeometry' with a method 'area' that raises an exception.
"""


class BaseGeometry:
    """
    A base class for geometry-related functionality.
    """

    def area(self):
        """
        Raises an exception indicating that the 'area' method is not implemented.

        Parameters: None
        Raises: Exception
        """
        raise Exception("area() is not implemented")
