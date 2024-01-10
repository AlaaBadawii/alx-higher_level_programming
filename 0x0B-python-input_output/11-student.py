#!/usr/bin/python3
"""``Student`` class module"""


class Student:
    """A class that represent a student"""

    def __init__(self, first_name, last_name, age):
        """sets attributes of a new student instance

            Args:
            first_name (str): first name
            last_name (str): last name
            age (int): the age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a json represent of student"""
        r = {}
        if attrs is not None:
            keys = [key for key in self.__dict__ if key in attrs]
        else:
            keys = [key for key in self.__dict__]

        for key in keys:
            value = getattr(self, key)
            if type(value) in [bool, int, str, dict, list]:
                r[key] = value
        return r

    def reload_from_json(self, json):
        """Replaces all attributs of Student instance from json"""
        for key in json:
            setattr(self, key, json[key])
