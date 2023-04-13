#!/usr/bin/python3
"""Module with class student define by public attributes"""


class Student:
    """ class that defines student by public attributes """

    def __init__(self, first_name, last_name, age):
        """ Def that initializes the public attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ method that retrives the dictionary rep """
        return self.__dict__
