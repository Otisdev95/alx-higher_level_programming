#!/usr/bin/python3
""" Module with a class MyInt that inherits from int """


class MyInt(int):
    """ Def of class MyInt that inherits from int """

    def __eq__(self, value):
        """ Inverting == operator to != """
        return int(self) != int(value)

    def __ne__(self, value):
        """ Inverting != operator to == """
        return int(self) == int(value)
