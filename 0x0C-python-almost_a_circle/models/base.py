#!/usr/bin/python3
""" models.base """
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init of the class"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)
