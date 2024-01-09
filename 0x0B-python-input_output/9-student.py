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
    def to_json(self):
        """Return a json represent of student"""
        r = {}
        for key in self.__dict__:
            value = getattr(self, key)
            if value in [bool, int, str, dict, list]:
                r[key] = value
        return r
