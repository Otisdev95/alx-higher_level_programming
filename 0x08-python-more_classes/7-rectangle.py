#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this represents the class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize the class Rectangle
        Args:
            height: represents the height of the rectangle
            width: represents the width of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attributes"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attributes"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """returns a string representation of the Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message for every object that gets deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
