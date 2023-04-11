#!/usr/bin/python3
""" Inherits from BaseGeometry (7-base_geometry.py) """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ 
        Class that inherits from BaseGeometry

        Instantiation:
            width (int): Width of the Rectangle.
            height (int): Height of the Rectangle.
    """

    def __init__(self, width, height):
        """ Initializes an instance of the class Rectangle """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
