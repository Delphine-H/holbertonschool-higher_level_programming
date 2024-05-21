#!/usr/bin/python3
"""
Module that contain a function that prints a square
"""


def print_square(size):
    """
    Function that prints a square with the character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    for row in range(size):
        for element in range(size):
            print("#", end="")
        print()
