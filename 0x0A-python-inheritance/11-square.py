#!/usr/bin/python3
""" Module defining a class Square that inherits from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Def of the class that inherits the Square """

    def __init__(self, size):
        """ Initializes an instance of class Square """

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Returns the method that implements area of the Square """

        area = self.__size ** 2
        return area

    def __str__(self):
        """ 
            Prints and returns the Square
            description in string representation
        """
        return "[{}] {}/{}".format(type(self).__name__, self.__size,
                                        self.__size)
