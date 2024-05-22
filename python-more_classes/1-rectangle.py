#!/usr/bin/python3
"""
Module that contain a class Rectangle
"""


class Rectangle:
    "Class that defines a Rectangle"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("La largeur doit être un entier")
        if value < 0:
            raise ValueError("La largeur doit être >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("La hauteur doit être un entier")
        if value < 0:
            raise ValueError("La hauteur doit être >= 0")
        self.__height = value
