#!/usr/bin/python3
"""
Base class for all models
"""

import json
import os


class Base:
    """
    Base class for all models
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        if list_objs is None or len(list_objs) == 0:
            with open(filename, "w") as f:
                f.write("[]")
        else:
            with open(filename, "w") as f:
                f.write(cls.to_json_string(list(map(lambda x:
                                                    x.to_dictionary(),
                                                    list_objs))))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return [cls.create(**d) for d in
                        cls.from_json_string(f.read())]
        return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw the rectangles and squares
        """
        t = turtle.Turtle()
