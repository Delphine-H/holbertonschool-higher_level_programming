#!/usr/bin/python3
"""A class Square"""


class Square:
    """A Square class that devine a square"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """instance attribute"""
        self.__size = size
