#!/usr/bin/python3
""" Module with function that reads a text file and prints it to stdout """


def read_file(filename=""):
    """ Def of file that reads a UTF-8 text file and prints to stdout """

    with open(filename, 'r', encoding="utf-8") as myFile:
        print(myFile.read(), end="")
