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

    # stactic methods
    @staticmethod
    def isVaildInt(attr, obj):
        """checks if an attribute is a vaild integer"""
        if not isinstance(obj, int):
            raise TypeError(f"{attr} must be an integer")
        if attr in ["width", "height"] and obj <= 0:
            raise ValueError(f"{attr} must be > 0")
        if attr in ["x", "y"] and obj < 0:
            raise ValueError(f"{attr} must be >= 0")

    # width
    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        self.isVaildInt("width", value)
        self.__width = value

    # height
    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        self.isVaildInt("height", value)
        self.__height = value

    # x
    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, value):
        self.isVaildInt("x", value)
        self.__x = value

    # y
    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, value):
        self.isVaildInt("y", value)
        self.__y = value

    # instance methods
    def area(self):
        """returns the area value of the Rectangle."""
        return self.height * self.width

    def display(self):
        """prints in stdout the Rectangle instance
        with the character #"""
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            if self.x > 0:
                print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
