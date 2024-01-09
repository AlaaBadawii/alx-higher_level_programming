#!/usr/bin/python3
def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout:
    Args:
        filename (file): name of the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_file = f.read()
    print(read_file, end="")
