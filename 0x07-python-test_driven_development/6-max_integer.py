#!/usr/bin/python3
"""Module to find the max integer in a list"""


def max_integer(list=[]):
    """
    A function that finds and returns the amx ineteger in a list of integers
    If the the list is empty -  the function returns None
    """
    if len(list) == 0:
        return None
    outcome = list[0]
    i = 1
    while i < len(list):
        if list[i] > outcome:
            outcome = list[i]
        i += 1
    return outcome
