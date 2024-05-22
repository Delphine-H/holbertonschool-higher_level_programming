#!/usr/bin/python3
"""
Module that contain a class Rectangle
"""


class Rectangle:
    "Class that defines a Rectangle"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        my_rectangle = ""
        if self.__height != 0 or self.__width != 0:
            for row in range(self.__height):
                my_rectangle += '#' * self.width
                if row < self.__height - 1: 
                    my_rectangle += "\n"
        return my_rectangle

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
