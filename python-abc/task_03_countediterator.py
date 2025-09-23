#!/usr/bin/env python3
"""CountedIterator class"""


class CountedIterator:
    """Class that wraps an iterator and counts the number of element"""

    def __init__(self, iterator):
        """Constructor of the class."""
        self.iterator = iter(iterator)
        self.count = 0

    def get_count(self):
        """Returns the number of elements"""
        return self.count

    def __next__(self):
        """Retrieves the next element from the iterator."""
        try:
            value = next(self.iterator)
            self.count += 1
            return value
        except StopIteration:
            raise StopIteration
