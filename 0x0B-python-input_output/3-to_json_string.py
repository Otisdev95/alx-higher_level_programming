#!/usr/bin/python3
"""
    Module with a function that returns the
    JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """ Def that returns JSON to string """
    return json.dumps(my_obj)
