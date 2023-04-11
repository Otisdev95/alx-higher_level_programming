#!/usr/bin/python3
""" Module that defines a class BaseGeometry """


class BaseGeometry:
    """ Def of the class BaseGeometry """

    def area(self):
        """
            Public instance method that raises an
            Exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Public instance method that validates an int

            Args:
                name: Is always a string

            Raises:
                TypeError: If the value is not an int.
                ValueError: If value is less or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
