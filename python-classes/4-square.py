#!/usr/bin/python3

"""Access and update private attribute """

class Square:
    def __init__(self, size=0):
        self.__size = size
        
    @property
    def size(self):
        """
        Getter method for the size attribute.
        Return:
            int: The size of the square.
        """
        
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value
        
    def area(self):
        return self.__size**2
