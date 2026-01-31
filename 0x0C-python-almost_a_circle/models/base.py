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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"

        if list_objs is None:
            json_str = cls.to_json_string([])
        else:
            dicts = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(dicts)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                json_data = f.read()

            str_data = cls.from_json_string(json_data)
            list_instance = [cls.create(**d) for d in str_data]

            return list_instance

        except FileNotFoundError:
            return []
