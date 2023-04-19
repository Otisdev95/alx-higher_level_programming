#!/usr/bin/python3
"""
    Module with class Square inheriting
    from the class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square inheriting from a Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square"""
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string rep of the class"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """size getter function"""
        return self.__width

    @size.setter
    def size(self, newSize):
        """size setter function"""
        if type(newSize) != int:
            raise TypeError("width must be an integer")
        if newSize <= 0:
            raise ValueError("width must be > 0")
        self.__width = newSize
        self.__height = newSize

    def update(self, *args, **kwargs):
        """
            updates the class by adding the public method
            that assigns attributes
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

        def to_dictionary(self):
            """dictionary representation of a Square"""
            squareDict = {
                'size': self.size, 'x': self.x,
                'y': self.y, 'id': self.id}
            return squareDict
