 #!/usr/bin/python3
"""
Module that contain a load_from_json_file function
"""

import json

def load_from_json_file(filename):
	"""function that crates an Object from a JSON File"""
	with open(filename, encoding="utf8") as my_file:
		return json.load(my_file)
