#!/usr/bin/python3
"""A class Square"""


class Square:
    """A Square class that devine a square"""

    def __init__(self, size=0):
        """instance attribute"""
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area of square"""
        return self.__size**2

    def my_print(self):
        """Print square"""
        for row in range(self.size):
            for column in range(self.size):
                print("#", end="")
            print("")
