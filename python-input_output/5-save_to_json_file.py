#!/usr/bin/python3
"""
This module contain a save_to_json_file function
"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a JSON file"""
    with open(filename, "w", encoding="utf8") as my_file:
        json.dump(my_obj, my_file)
