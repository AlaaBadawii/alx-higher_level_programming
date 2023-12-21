#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """represent a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """initial position"""
        self.__position = position
        self.__size = size

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

    @property
    def position(self):
        """retrive square position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set position of the square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calc area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints  the square with the character #"""
        if self.__size == 0:
            print()
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
