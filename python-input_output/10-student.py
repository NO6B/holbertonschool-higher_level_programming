#!/usr/bin/python3
"""Student class"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary representation of a Student"""
        if isinstance(attrs, list):
            value = {}
            for i in attrs:
                if hasattr(self, i):
                    value[i] = getattr(self, i)
            return value

        return self.__dict__
