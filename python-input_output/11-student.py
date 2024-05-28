#!/usr/bin/python3
"""
This module contain a class Student
"""


class Student:
    """class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """initialize a new student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrives a dictionary representation of a student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: self.__dict__[attr]
                for attr in attrs if attr in self.__dict__
            }

    def reload_from_json(self, json):
        """replaces all attributes of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)
