#!/usr/bin/python3
"""
This module read data from CSV and converting it into
a format JSON using serialization techniques
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Function that convert CSV filename and writes the JSON data

    Args:
            filename (str): name of the CSV file

    Returns:
            True if the conversion is successful
    """
    try:
        with open(filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        with open("data.json", "w") as json_file:
            json.dump(data, json_file)
        return True
    except Exception as e:
        print(f"An error occured while converting CSV to JSON: {e}")
        return False
