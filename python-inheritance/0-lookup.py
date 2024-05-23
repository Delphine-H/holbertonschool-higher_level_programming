#!/usr/bin/python3
"""
Module that contain a function who return
a list of available attributes and methods of an object
"""


def lookup(obj):
    """
    function that returns a list of available
    attributes and methods of an object
    """
    return dir(obj)
