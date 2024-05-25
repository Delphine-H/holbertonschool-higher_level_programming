#!/usr/bin/python3
"""
This method contain a CountedIterator class
"""


class CountedIterator:
    """
    Class that extends the built-in iterator
    """

    def __init__(self, iterable):
        """initialise attributs"""
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """add counter"""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """retrive the number of items"""
        return self.counter
