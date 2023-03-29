#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """Initializing this square class
    Args:
        size: represnets the size of the square defined
    Raises:
        TypeError: if size is not integer
        ValueError: if size is less than zero
    """

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)