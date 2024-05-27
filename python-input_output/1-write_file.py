#!/usr/bin/python3
"""
This module contain a function write file
"""


def write_file(filename="", text=""):
    """write the text in file and return number of characters"""
    with open(filename, "w", encoding="utf8") as my_file:
        return my_file.write(text)
