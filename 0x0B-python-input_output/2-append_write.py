#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    Args:
        filename (file): name of the file
        text (string): string to be written
    Returns:
         returns the number of characters written
    """
    char_written = 0
    with open(filename, 'a', encoding="utf-8") as f:
        char_written = f.write(text)
    return char_written
