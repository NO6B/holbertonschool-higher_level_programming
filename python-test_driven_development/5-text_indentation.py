#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Args:
        text: The text to be printed.
    raises:
        TypeError: If `text` is not a string.
    
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for i in text:
        line += i
        if i in ".?:":
            print(line.strip())
            print()
            line = ""
