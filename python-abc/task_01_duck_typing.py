#!/usr/bin/python3
"""
Module that contain a class Shape and 2 subclass
Circle and rectangle
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Class shape that inherit ABC
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Class Circle that inherit Shape
    """

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("radius must be >= 0")
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class Rectangle that inherit Shape
    """

    def __init__(self, width, height):
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Standalone function shape_info
    """
    print("Aera:", shape.area())
    print("Perimeter:", shape.perimeter())
