#!/usr/bin/python3
""" rectangle """
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # width
    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    # height
    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    # x
    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    # y
    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
