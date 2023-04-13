#!/usr/bin/python3
"""
    Module with function that appends a string at the end of a
    text file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
        Def of file that append a string at
        the end of a UTF-8 text file
    """

    with open(filename, 'a', encoding="utf-8") as myFile:
        return myFile.write(text)
