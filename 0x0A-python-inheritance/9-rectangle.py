#!/usr/bin/python3
""" Module defining a class Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ 
        Def of the class that inherits the BaseGeometry
        Instantiation:
            width (int): Width of the Rectangle.
            height (int): Height of the Rectangle.
    """

    def __init__(self, width, height):
        """ Initializes an instance of class Rectangle """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns the method that implements area Rectangle """

        area = self.__width * self.__height
        return area

    def __str__(self):
        """ Return and Print the Rectangle description """

        return "[{}] {}/{}".format(type(self).__name__, self.__width,
                                                    self.__height)
