#!/usr/bin/python3
"""

This module contain a class BaseGeometry

"""


class BaseGeometry:
    """
    Class BaseGeometry with a methode area
    """

    def __init__(self):
        pass

    def area(self):
        """
        methode to be implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        methode that validate value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
