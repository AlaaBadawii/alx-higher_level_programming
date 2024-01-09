#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Args:
        filename (file): name of the file
        text (string): string to be written
    Returns:
         returns the number of characters written
    """
    char_written = 0
    with open(filename, 'w', encoding="utf-8") as f:
        char_written = f.write(text)
    return char_written
