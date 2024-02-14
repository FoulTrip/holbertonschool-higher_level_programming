#!/usr/bin/python3

""" Square class definition """


class Square:
    """A class to represent a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Constructor method for Square class.

    Args:
        size (int): The size of the square.

    """

    def __init__(self, size):
        """Initializes a new Square object with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
