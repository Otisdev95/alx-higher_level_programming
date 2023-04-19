#!/usr/bin/python3
"""Module containing the first class base"""

import json
import csv
import os


class Base:
    """Base class with private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """def of class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method returning JSON representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """methods that writes JSON str rep of list_objs to a file"""
        fileName = cls.__name__ + ".json"
        if list_objs is None:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        with open(fileName, 'w') as fn:
            fn.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string representation json_string"""
        json_string_list = []
        if json_string is not None and json_string != "":
            json_string_list = json.loads(json_string)
        else:
            return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """def that returns an instance with all attributes set already"""
        if cls.__name__ == "Rectangle":
            dummyIns = cls(1, 1)
        elif cls.__name__ == "Square":
            dummyIns = cls(1)

        dummyIns.update(**dictionary)
        return dummyIns

    @classmethod
    def load_from_file(cls):
        """method that returns a list of instances"""
        fileName = "{}.json".format(cls.__name__)
        ins = []
        dict_list = []

        if os.path.exists(fileName):
            with open(fileName, 'r') as fn:
                j_str = fn.read()
                dict_list = cls.from_json_string(j_str)
                for dic in dict_list:
                    ins.append(cls.create(**dic))
        return ins
