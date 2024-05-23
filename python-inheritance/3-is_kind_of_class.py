#!/usr/bin/python3
"""
This module contain a function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    function that returns True if the object is an instance
    of or an instance of inherited class
    """
    return isinstance(obj, a_class)
