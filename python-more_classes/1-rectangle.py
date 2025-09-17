#!/usr/bin/python3
"""Defines an empty Rectangle class"""


class Rectangle:
    """empty rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise TypeError("width must be >= 0")

    @property
    def height(self):
        """retrive height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value of height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif self.__height < 0:
            raise TypeError("width must be >= 0")
