#!/usr/bin/python3
"""
This module contain function inherits_from
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an insance
    of a class that inerited from the specified class
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
