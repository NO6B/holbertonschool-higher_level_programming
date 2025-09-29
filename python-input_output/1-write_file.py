#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""
    count = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        for i in text:
            f.write(i)
            count += 1
    return count
