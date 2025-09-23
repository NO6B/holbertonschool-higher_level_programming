#!/usr/bin/env python3
"""Verboselist class"""


class VerboseList(list):
    def append(self, object):
        super().append(object)
        print("Added [{}] to this list.".format(object))

    def extend(self, iterable):
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, value):
        print("Removed [{}] from the list.".format(value))
        super().remove(value)

    def pop(self, index=-1):
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        super().pop(index)
