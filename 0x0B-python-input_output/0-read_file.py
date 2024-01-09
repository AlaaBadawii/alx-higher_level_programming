#!/usr/bin/python3
"""``read_file`` module"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout:
    Args:
        filename (file): name of the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
