#!/usr/bin/env python3
"""Verboselist class"""


class VerboseList(list):
    """class VerboseList that inherits from the built-in list class."""

    def append(self, object):
        """Add an object to the list and print a message"""
        super().append(object)
        print("Added [{}] to the list.".format(object))

    def extend(self, iterable):
        """extending the list,"""
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, value):
        """remove methode"""
        print("Removed [{}] from the list.".format(value))
        super().remove(value)

    def pop(self, index=-1):
        """pop methode"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        super().pop(index)
