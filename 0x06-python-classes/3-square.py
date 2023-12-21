#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """represent a Square"""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): the size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)
