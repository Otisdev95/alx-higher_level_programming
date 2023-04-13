#!/usr/bin/python3
"""
    Module with a function that returns an object
    (Python data structure) represented by a JSON string
"""

import json


def from_json_string(my_str):
    """ Def funtion that returns object rep by JSON string """
    return json.loads(my_str)
