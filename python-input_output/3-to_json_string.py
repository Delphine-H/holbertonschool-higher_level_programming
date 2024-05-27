#!/usr/bin/python3
"""
This module contain a function to_json_string
"""

import json


def to_json_string(my_obj):
    """function that return a representation of an object JSON"""
    return json.dumps(my_obj)
