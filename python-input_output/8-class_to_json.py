#!/usr/bin/python3
"""
This module contain a function class_to_json
"""


def class_to_json(obj):
	"""function that returns the dictionary description of an object"""
	return vars(obj)