#!/usr/bin/python3
"""
This module contain functions that adds the functionality to serialize
a Python dictionary to a JSON file and deserialize the JSON
file to recreate the Python Dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Function that serialize and save data to the specified file

    Args:
        data (dict): a Python dictionary with data

        filename (str): filename of the output JSON file. If already exits
        it should be replace.

    """
    with open(filename, "w") as my_file:
        json.dump(data, my_file)


def load_and_deserialize(filename):
    """
    Function that load and deserialize data from the specified file

    Args:
        filename (str): the name of the input JSON file

    Returns:
        A Python dictionary with deserialized JSON data
    """
    with open(filename, "r") as my_file:
        return json.load(my_file)
