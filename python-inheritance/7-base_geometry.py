#!/usr/bin/python3

"""
This script defines a class 'BaseGeometry' with a method 'area' that raises an exception,
and a method 'integer_validator' to validate integer values.
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

    def integer_validator(self, name, value):
        """
        Validates an integer value.

        Parameters:
        - name: Name of the value being validated.
        - value: The value to be validated.

        Raises:
        - ValueError if the value is not greater than 0.
        - TypeError if the value is not an integer.
        """
        if type(value) == int:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
        else:
            raise TypeError(f"{name} must be an integer")
