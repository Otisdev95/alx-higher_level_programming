#!/usr/bin/python3
"""
    Module with a function that writes an Object
    to a text file, using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """ def that writes an object to a text file using JSON """
    with open(filename, "w",) as myFile:
        json.dump(my_obj, myFile)
