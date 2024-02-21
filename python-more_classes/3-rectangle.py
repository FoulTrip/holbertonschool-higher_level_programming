#!/usr/bin/python3
""" Area and Perimeter"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Initializes the rectangle with optional width and height."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""

        return "\n".join(["#" * self.width] * self.height)
