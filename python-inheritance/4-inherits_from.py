#!/usr/bin/python3
"""function inherits_from"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
