#!/usr/bin/python3
"""Defines an empty class Square"""


class Square:
    """Args:
            Private instance attribute: size
        Raises:
            TypeError: if size is less than 0, raise a ValueError
   """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    def position(self):
        """Return position"""
        return self.__position

    def position(self, value):
        """property setter position """
        if (
            isinstance(value, tuple) and
            len(value) == 2
        ):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, (int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return:
                returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()

        for j in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
