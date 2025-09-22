#!/usr/bin/python3
"""function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of a_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
