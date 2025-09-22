#!/usr/bin/python3
"""BaseGeomery Class"""


class BaseGeometry:
    """empty class"""
    def __init__(self, width, height):
        pass

    def area(self):
        """method that raises an Exception with the message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initializes variables and methods"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
