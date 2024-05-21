#!/usr/bin/python3
"""
Defines add_integer(a, b=98) that adds two integers or floats.
This function takes two arguments and returns their sum
after converting them to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after converting them to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
