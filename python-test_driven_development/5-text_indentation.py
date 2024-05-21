#!/usr/bin/python3
"""
Module that contain a function that add new lines in a test
"""


def text_indentation(text):
    """
    Function that print 2 new lines after .?: characters;
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        split_text = text.split(delim)
        stripped_lines = []
        for line in split_text:
            stripped_lines.append(line.strip(" "))
            text = (delim + "\n\n").join(stripped_lines)

    print(text, end="")
