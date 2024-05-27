#!/usr/bin/python3
"""
This module contain a function read_file
"""


def read_file(filename=""):
    """function that open a file"""
    with open(filename, encoding="utf-8") as my_file:
        for my_line in my_file:
            print(my_line, end="")
