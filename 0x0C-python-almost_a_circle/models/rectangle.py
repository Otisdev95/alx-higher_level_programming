#!/usr/bin/python3
"""
    Module with class Rectangle inheriting
    from the super class Base
"""
from models.base import Base


class Rectangle(Base):
    """class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """def the class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    #getter function for width
    @property
    def width(self):
        """width getter function"""
        return (self.__width)

    #setter function for width
    @width.setter
    def width(self, newWidthValue):
        """width setter function"""

        if (type(newWidthValue) is not int):
            raise TypeError("width must be an integer")

        if newWidthValue <= 0:
            raise ValueError("width must be > 0")
        self.__width = newWidthValue

    #getter function for height
    def height(self):
        """height getter function"""
        return (self.__height)

    #setter function for height
    @height.setter
    def height(self, newHeightValue):
        """height setter function"""

        if (type(newHeightValue) is not int):
            raise TypeError("height must be an integer")

        if newHeightValue <= 0:
            raise ValueError("height must be > 0")
        self.__height = newHeightValue

    #getter function for x
    def x(self):
        """x getter function"""
        return (self.__x)

    #setter function for x
    @x.setter
    def x(self, newX):
        """ x setter function"""

        if (type(newX) is not int):
            raise TypeError("x must be an integer")

        if newX < 0:
            raise ValueError("x must be >= 0")
        self.__x = newX

    #getter function for y
    def y(self):
        """y getter function"""
        return (self.__y)

    #setter function for y
    @y.setter
    def y(self, newY):
        """ y setter function"""

        if (type(newY) is not int):
            raise TypeError("y must be an integer")

        if newY < 0:
            raise ValueError("y must be >= 0")
        self.__y = newY

    def area(self):
        """def that calculates the area of Rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """def that prints in stdout the Rectangle with character #"""
        for y in range(self.y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """def that returns the string format of Rectange"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(\
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                    self.__init__(self.__width, self.__height, self.__x, self.__y)
                else:
                    self.id = arg
                elif a == 1:
                    self.__width = arg
                elif a == 2:
                    self.__height = arg
                elif a == 3:
                    self.__x = arg
                elif a == 4:
                    self.__y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.__width, self.__height, self.__x, self.__y)
                    else:
                        self.id = value
                    elif key == "width":
                        self.__width = value
                    elif key == "height":
                        self.__height = value
                    elif key == "x":
                        self.__x = value
                    elif key == "y":
                        self.__y = value

    def to_dictionary(self):
        """dictionary representation of a rectangle"""
        recDict = {"id": self.id, "width": self.__width,
                    "height": self.__height,
                    "x": self.__x, "y": self.__y}
        return recDict
