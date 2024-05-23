#!/usr/bin/python3
"""
This module contain a class Rectangle that inherit
from BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherit from BaseGeometry
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        self.integer_validator("width", width)

    def aera(self):
        """Methode that eturn the area"""
        return self.__width * self.__height

    def __str__(self):
        """This method returns a string representation"""
        return "[{}] {}/{}".format(
            self.__class__.__name__, self.__width, self.__height)
