#!/usr/bin/python3
"""
This module contain a Square class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    class Square that inherit of Rectangle class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
    
    def __str__(self):
        """This method returns a string representation"""
        return "[Square] {}/{}".format(
            self.__size, self.__size)
    