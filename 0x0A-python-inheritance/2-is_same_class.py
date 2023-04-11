#!/usr/bin/python3
"""Module that returns True or False"""


def is_same_class(obj, a_class):
    """
        Function that returns True is if
        the obj is exactly an instance of
        the specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
