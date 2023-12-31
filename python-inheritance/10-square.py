#!/usr/bin/python3

"""Square #1 """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
