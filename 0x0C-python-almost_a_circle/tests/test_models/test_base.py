#!/usr/bin/python3
""" Module containing test cases for the base """

import os
import json
import unittest
from models.base import Base
from models.square import Square


class test_base(unittest.TestCase):
    """ Test to validate the base """

    def setUp(self):
        """ Test to set up """
        pass

    def tearDown(self):
        """ Tear down after test """
        try:
            os.remove("Square.json")
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_id(self):
        """ Passing a valid id """
        self.assertEqual(Base(20).id, 20)

    def test_no_id(self):
        """ Passing in no id """
        self.assertEqual(Base().id, 1)

    def test_negative_id(self):
        """ Passing in a -ve id """
        self.assertEqual(Base(-5).id, -5)

    def test_float_id(self):
        self.assertEqual(Base(5.5).id, 5.5)

    def test_excess_attr(self):
        """ Passing in too many attributes """
        with self.assertRaises(TypeError):
            Base(1, 2, 3, 4)

    def test_list_id(self):
        """ Passing in a list id """
        self.assertEqual(Base([1, 2, 3, 4]).id, [1, 2, 3, 4])

    def test_string_id(self):
        """ Passing in a string id """
        self.assertEqual(Base("Otis").id, "Otis")

    def test_to_json(self):
        """ Passing in a JSON type """
        obj = Square(1, 2, 3, 4)
        obj_dict = obj.to_dictionary()
        json_string = Base.to_json_string([obj_dict])
        self.assertEqual(type(json_string), str)

    def test_from_json(self):
        """ Passing in JSON types """
        obj = Square(1, 2, 3, 4)
        obj_dict = obj.to_dictionary()
        json_string = Base.to_json_string([obj_dict])
        list_dict = Base.from_json_string(json_string)
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(type(json_string), str)
        self.assertEqual(type(list_dict), list)

    def test_to_json_string_empty(self):
        """ Passing in an empty string """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_None(self):
        """ Passing in a None """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_create(self):
        """ Passing in the dict of obj """
        sq1 = Square(5, 10, 5, 10)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertIsNot(sq1,sq2)
