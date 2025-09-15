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
        if not isinstance(size, (int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
