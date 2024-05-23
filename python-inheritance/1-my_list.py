#!/usr/bin/python3
"""
Module that contain a MyList class who inherits from list
"""


class MyList(list):
    """
    class that inherits from list
    """

    def print_sorted(self):
        print(sorted(self))
