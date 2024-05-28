#!/usr/bin/python3
"""
This module explore serialization and deserialization using XML as an alternative
format to JSON
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Function that serialize a dictionary in XML and save in filename"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Function that read the XML and deserialized Python dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
