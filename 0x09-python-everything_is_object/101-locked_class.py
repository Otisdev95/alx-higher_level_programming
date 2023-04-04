#!/usr/bin/python3
"""This function defines a locked class with no class or object attribute"""


class LockedClass:
    """
        Only allows instatiation of an attribute called first_name.
    """

    __slots__ = ["first_name"]
