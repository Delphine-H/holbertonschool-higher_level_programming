#!/usr/bin/python3

from abc import ABC, abstractmethod
import math

"""
Module that contain a class Shape and 2 subclass
Circle and rectangle
"""


class Shape(ABC):
    """
    Class shape that inherit ABC
    """
    @abstractmethod
    def area(self):
        """Area method"""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimeter method"""
        pass


class Circle(Shape):
    """
    Class Circle that inherit Shape
    """
    def __init__(self, radius):
        """Circle constructor"""
        self.radius = abs(radius)

    def area(self):
        """Area method cicle"""
        return math.pi * self.radius**2

    def perimeter(self):
        """Perimeter method circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class Rectangle that inherit Shape
    """
    def __init__(self, width, height):
        """Rectangle constructor"""
        self.width = width
        self.height = height

    def area(self):
        """Area method rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter method rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Standalone function shape_info
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
