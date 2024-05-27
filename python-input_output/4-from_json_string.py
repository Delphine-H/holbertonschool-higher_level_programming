#!/usr/bin/python3
""""
This module contain a from_json_string
"""


import json


def from_json_string(my_str):
    """function that return a python data structure"""
    return json.loads(my_str)
