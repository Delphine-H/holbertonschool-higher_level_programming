#!/usr/bin/python3
"""
This module contain a class BaseGeometry
"""


class BaseGeometry:
    """
    Class BaseGeometry with a methode area
    """

    def area(self):
        """methode to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """methode that validate value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
