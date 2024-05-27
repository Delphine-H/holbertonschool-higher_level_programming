#!/usr/bin/python3
"""
This module contain a function read_file
"""


def read_file(filename=""):
    """function that open a file"""
    with open(filename, encoding="utf-8") as my_file:
        for l in my_file:
            print(l, end="")
