#!/usr/bin/python3

"""Size validation """


class Square:
    """A class to represent a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Constructor method for Square class.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """Initializes a new Square object with an optional size parameter.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
