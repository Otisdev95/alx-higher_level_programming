#!/usr/bin/python3
"""
    Module with function that writes a string to a text
    file and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ Def of file that write a string to a UTF-8 text file  """

    with open(filename, 'w', encoding="utf-8") as myFile:
        return myFile.write(text)
