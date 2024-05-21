#!/usr/bin/python3
"""
Defines a function add_integer(a, b=98) that adds two integers.

Attributes:
    add_integer: function that adds two integers.
"""

def add_integer(a, b=98):
    '''
    Function that adds 2 integers.

    Parameters:
    	a (int, float): The first number.
    	b (int, float, optional): The second number, default is 98.

    Returns:
    	int: The sum of the two numbers, converted to an integer.

    Exceptions:
    	TypeError: If a or b are not integers or floats.
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    
    return int(a) + int(b)


