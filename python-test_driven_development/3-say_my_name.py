#!/usr/bin/python3
"""
function that prints
"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is

    args:
        <first name: (str): The first name
        <last name: (str): The last name

    Raises:
        TypeError: If first_name or last_name is not a string.


    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
