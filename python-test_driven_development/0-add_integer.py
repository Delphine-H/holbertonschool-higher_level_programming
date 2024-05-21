#!/usr/bin/python3
"""
Defines add_integer(a, b=98) that adds two integers or floats.
This function takes two arguments and returns their sum
after converting them to integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats after converting them to integers.

    Args:
        a: First number (int or float).
        b: Second number (int or float), default is 98.

    Returns:
        The sum of the two numbers as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
