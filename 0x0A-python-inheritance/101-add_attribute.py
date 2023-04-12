#!/usr/bin/python3
""" Module that adds new attribute to object """


def add_new_attribute(obj, name, value):
    """ Def the method for adding the new attribute """

    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
