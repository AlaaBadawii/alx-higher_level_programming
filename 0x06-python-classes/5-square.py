#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """represent a Square"""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """to retrive the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """check i value and type are vaild"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calc area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """ prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
