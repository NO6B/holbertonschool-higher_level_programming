#!/usr/bin/python3
"""Defines an empty class Square"""


class Square:
    """Args:
            Private instance attribute: size
        Raises:
            TypeError: if size is less than 0, raise a ValueError
   """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.__size = value
        if not isinstance(value, (int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """return:
                returns the current square area"""
        return self.__size ** 2
