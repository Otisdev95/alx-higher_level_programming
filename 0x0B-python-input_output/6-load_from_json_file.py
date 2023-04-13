#!/usr/bin/python3
"""Module with a function that creates an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """def of funct that creates an Object from a JSON file"""
    with open(filename, 'r') as myFile:
        return json.load(myFile)
