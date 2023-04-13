#!/usr/bin/python3
"""
    Module with a script that adds all arguments
    to a Python list, and then save them to a file
"""

import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        pythonList = load_from_json_file("add_item.json")
    except FileNotFoundError:
        pythonList = []
    pythonList.extend(sys.argv[1:])
    save_to_json_file(pythonList, "add_item.json")
