#!/usr/bin/python3
"""
This module contain a function append_write
"""


def append_write(filename="", text=""):
    """function that append text at the end of the file"""
    with open(filename, "a", encoding="utf8") as my_file:
        return my_file.write(text)
